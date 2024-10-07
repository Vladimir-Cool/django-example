from django.contrib import admin
from .models import CmsSlider


@admin.register(CmsSlider)
class CmsSliderAdmin(admin.ModelAdmin):
    list_display = 'id', 'cms_title', 'cms_text', 'cms_css', 'cms_url',
    list_display_links = 'id', 'cms_title'

