from django.contrib import admin
from .models import PriceCard, PriceTable


@admin.register(PriceCard)
class PriceCardAdmin(admin.ModelAdmin):
    list_display = 'id', 'pc_value', 'pc_description'
    list_display_links = 'id', 'pc_value'


@admin.register(PriceTable)
class PriceTableAdmin(admin.ModelAdmin):
    list_display = 'id', 'pc_title', 'pc_old_price', 'pc_new_price'
    list_display_links = 'id', 'pc_title'

