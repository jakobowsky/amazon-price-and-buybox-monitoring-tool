
from django.contrib import admin
from monitoring.models import (
    Asin,
    DataRow,
)


class DataRowAdmin(admin.ModelAdmin):
    list_display = ["asin", "created_at", 'listing_price', 'shipping_price', 'seller_feedback_count', 'seller_positive_feedback_rating', 'is_buy_box_winner',]
    search_fields = ["asin__asin"]
    list_filter = ["is_buy_box_winner", 'asin']


admin.site.register(Asin)
admin.site.register(DataRow, DataRowAdmin)
