from django.http import HttpRequest, HttpResponse
from django.urls import reverse
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView


from .models import Order, StatusCrm
from .forms import OrderForm
from ex_cms.models import CmsSlider
from price.models import PriceCard, PriceTable

def index_page(request: HttpRequest) -> HttpResponse:
    objects_list = Order.objects.all()
    slider_list = CmsSlider.objects.all()
    price_table = PriceTable.objects.all()
    pc1, pc2, pc3 = PriceCard.objects.all()[:3]
    form = OrderForm()

    contex = {
        'objects_list': objects_list,
        'slider_list': slider_list,
        'price_table': price_table,
        'price_card': {'pc1': pc1,
                       'pc2': pc2,
                       'pc3': pc3},
        'form': form,
    }

    return render(request, 'index.html', context=contex)


def thanks_page(request):
    print(request.POST)
    new_order = Order(order_name=request.POST['order_name'],
                      order_phone=request.POST['order_phone'],
                      order_status=StatusCrm.objects.get(status_name='Новый'))
    new_order.save()
    return render(request, 'thanks.html', context={'new_order': new_order})



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

