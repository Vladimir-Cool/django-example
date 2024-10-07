from django.contrib import admin
from .models import Order, StatusCrm, CommentCrm

# admin.site.register(Order)
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """ Регистрация модели в admin панели"""
    # Список полей которые будут отражаться в админке на странице модели.
    list_display = 'id', 'order_name', 'order_phone', 'order_status', 'order_dt'
    # Список полей на которых будет ссылка для перехода на страницу записи
    list_display_links = 'id', 'order_name'


@admin.register(StatusCrm)
class StatusCrmAdmin(admin.ModelAdmin):
    list_display = 'id', 'status_name'
    list_display_links = 'id', 'status_name'


@admin.register(CommentCrm)
class CommentCrmAdmin(admin.ModelAdmin):
    list_display = 'id', 'comment_text', 'comment_binding', 'comment_dt'
    list_display_links = 'id', 'comment_text'
