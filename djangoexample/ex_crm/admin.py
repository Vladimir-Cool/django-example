from django.contrib import admin
from .models import Order

# admin.site.register(Order)
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """ Регистрация модели в admin панели"""

    # Список полей которые будут отражаться в админке на странице модели.
    list_display = 'id', 'order_name', 'order_phone', 'order_dt'
    # Список полей на которых будет ссылка для перехода на страницу записи
    list_display_links = 'id', 'order_name'

