from django.http import HttpRequest, HttpResponse
from django.urls import reverse
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView


from .models import Order
from .forms import OrderForm
from ex_cms.models import CmsSlider


def index_page(request: HttpRequest) -> HttpResponse:
    objects_list = Order.objects.all()
    slider_list = CmsSlider.objects.all()
    return render(request, 'base.html', {'objects_list': objects_list, 'slider_list': slider_list})


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


#________________Примеры_для_работы_________________
# class OrderPreview(ListView):
#     template_name = 'ex_crm/index.html'
#     queryset = Order.objects.all()[:2]
#     context_object_name = 'objects_list'
#
# class OrderListView(ListView):
#     template_name = 'ex_crm/list.html'
#     model = Order
#     context_object_name = 'objects_list'
#
# class OrderDetailView(DetailView):
#     template_name = 'ex_crm/detail.html'
#     model = Order
#     context_object_name = 'order'
#
#
# class OrderCreateView(CreateView):
#     model = Order
#     form_class = OrderForm
#     template_name = 'ex_crm/form.html'

    # Если в классе модели определен метод get_absolute_url то он может заменить этот метод
    # def get_success_url(self):
    #     """ Вернет ссылку на страницу на которую будет переход после создания нового объекта"""
    #     return reverse('ex_crm:detail', kwargs={'pk': self.object.id})

