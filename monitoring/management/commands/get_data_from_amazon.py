from datetime import datetime

import pytz
from django.conf import settings
from django.core.management.base import BaseCommand

from sp_api.api import Products
from sp_api.base import SellingApiException, Marketplaces

from monitoring.models import Asin, DataRow

HEADER = [
    "id",
    "created_at",
    "updated_at",
    "asin",
    "marketplace_id",
    "shipping_currency",
    "shipping_price",
    "listing_currency",
    "listing_price",
    "shipping_max_hours",
    "shipping_min_hours",
    "shipping_availability",
    "sub_condition",
    "is_featured_merchant",
    "is_buy_box_winner",
    "is_fulfilled_by_amazon",
    "seller_feedback_count",
    "seller_positive_feedback_rating",
    "response",
    "date_of_request",
]


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.get_data_for_each_asin_and_save_to_db()

    def get_data_for_each_asin_and_save_to_db(self) -> None:
        for asin in Asin.objects.filter(is_running=True):
            try:
                self.get_pricing_from_amazon_for_asin(asin)
            except SellingApiException as e:
                print(f"Error with asin: {asin} :{e}")

    def get_pricing_from_amazon_for_asin(self, asin: Asin) -> None:
        client_config = dict(
            refresh_token=settings.REFRESH_TOKEN,
            lwa_app_id=settings.LWA_APP_ID,
            lwa_client_secret=settings.CLIENT_SECRET,
            aws_secret_key=settings.AWS_SECRET_KEY,
            aws_access_key=settings.AWS_ACCESS_KEY,
            role_arn=settings.ROLE_ARN,
        )
        res = Products(credentials=client_config, marketplace=Marketplaces.IT)
        return self.convert_response_to_amazon_pricing_list(
            res.get_item_offers(asin=asin.asin, item_condition="New").payload, asin
        )

    def convert_response_to_amazon_pricing_list(
            self, response_payload: dict, asin: Asin
    ) -> None:
        tz = pytz.timezone("Europe/Berlin")
        date_of_run = datetime.now(tz)
        for item in response_payload.get("Offers"):
            DataRow.objects.create(
                asin=asin,
                date_of_request=date_of_run,
                marketplace_id=response_payload.get("marketplaceId"),
                shipping_currency=item.get("Shipping", {}).get("CurrencyCode", ""),
                shipping_price=item.get("Shipping", {}).get("Amount", None),
                listing_currency=item.get("ListingPrice", {}).get("CurrencyCode", ""),
                listing_price=item.get("ListingPrice", {}).get("Amount", None),
                shipping_max_hours=item.get("ShippingTime", {}).get(
                    "maximumHours", None
                ),
                shipping_min_hours=item.get("ShippingTime", {}).get(
                    "minimumHours", None
                ),
                shipping_availability=item.get("ShippingTime", {}).get(
                    "availabilityType", ""
                ),
                sub_condition=item.get("SubCondition", ""),
                is_featured_merchant=item.get("IsFeaturedMerchant"),
                is_buy_box_winner=item.get("IsBuyBoxWinner"),
                is_fulfilled_by_amazon=item.get("IsFulfilledByAmazon"),
                seller_feedback_count=item.get("SellerFeedbackRating", {}).get(
                    "FeedbackCount", None
                ),
                seller_positive_feedback_rating=item.get(
                    "SellerFeedbackRating", {}
                ).get("SellerPositiveFeedbackRating", None),
                response=str(item), )
