from django.db import models
from django.utils.timezone import now


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        abstract = True


class Asin(BaseModel):
    asin = models.CharField(unique=True, max_length=250)
    is_running = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.asin}"


class DataRow(BaseModel):
    asin = models.ForeignKey(
        Asin, on_delete=models.CASCADE, related_name="data_rows"
    )
    date_of_request = models.DateTimeField(default=now)
    marketplace_id = models.CharField(max_length=250, default="")
    shipping_currency = models.CharField(max_length=250, default="")
    shipping_price = models.FloatField(null=True, blank=True)
    listing_currency = models.CharField(max_length=250, default="")
    listing_price = models.FloatField(null=True, blank=True)
    shipping_max_hours = models.FloatField(null=True, blank=True)
    shipping_min_hours = models.FloatField(null=True, blank=True)
    shipping_availability = models.CharField(max_length=250, default="")
    sub_condition = models.CharField(max_length=250, default="")
    is_featured_merchant = models.BooleanField(default=False)
    is_buy_box_winner = models.BooleanField(default=False)
    is_fulfilled_by_amazon = models.BooleanField(default=False)
    seller_feedback_count = models.IntegerField(null=True, blank=True)
    seller_positive_feedback_rating = models.FloatField(null=True, blank=True)
    response = models.TextField()

    def __str__(self):
        return f"{self.created_at} - {self.asin}"
