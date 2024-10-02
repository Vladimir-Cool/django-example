from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

from .models import Order


class OrderTestListIndexView(TemplateView):
    template_name = 'ex_crm/index.html'

    def get_context_data(self, **kwargs):
        """ Функция возвращает контекст для рендеринга Http ответа"""
        context = super().get_context_data(**kwargs)
        context['objects_list'] = Order.objects.all()
        return context


class OrderTestListView(ListView):
    """ Декларативный вид создания View"""
    # Шаблон на базе которого будем строить готовую html страницу
    template_name = 'ex_crm/list.html'
    # Указываем модель для получения Queryset.
    model = Order
    # Указываем Queryset если не нужно получить .objects.all()
    # queryset = Order.objects.all()
    # Имя переменной по которой мы хотим получить доступ к QuerySet в шаблоне
    context_object_name = 'objects_list'

def index_page(request: HttpRequest) -> HttpResponse:
    objects_list = Order.objects.all()
    return render(request, 'ex_crm/index.html', {'objects_list': objects_list})



#________________Примеры_для_работы_________________
class OrderPreview(ListView):
    template_name = 'ex_crm/index.html'
    queryset = Order.objects.all()[:2]
    context_object_name = 'objects_list'

class OrderListView(ListView):
    template_name = 'ex_crm/list.html'
    model = Order
    context_object_name = 'objects_list'

class OrderDetailView(DetailView):
    template_name = 'ex_crm/detail.html'
    model = Order
    context_object_name = 'order'




