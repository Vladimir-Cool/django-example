from django.urls import path
from django.views.generic import TemplateView


from .views import index_page, OrderPreview, OrderListView, OrderDetailView

# Переменная создает префикс для имен ссылок, чтобы они не пересекались.
app_name = 'ex_crm'

urlpatterns = [
    path('', OrderPreview.as_view(), name='home'),
    path('list/', OrderListView.as_view(), name='list'),
    path('detail/<int:pk>', OrderDetailView.as_view(), name='detail'),

    path('test/', TemplateView.as_view(template_name='ex_crm/index.html'), name='test'),

]