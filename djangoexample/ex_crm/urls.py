from django.urls import path
from django.views.generic import TemplateView


from .views import index_page, thanks_page

# Переменная создает префикс для имен ссылок, чтобы они не пересекались.
app_name = 'ex_crm'

urlpatterns = [
    path('', index_page, name='home'),
    path('thanks/', thanks_page, name='thanks_page'),
    # path('list/', OrderListView.as_view(), name='list'),
    # path('detail/<int:pk>', OrderDetailView.as_view(), name='detail'),
    # path('create/', OrderCreateView.as_view(), name='create'),
    # path('test/', TemplateView.as_view(template_name='ex_crm/index.html'), name='test'),

]