from django.shortcuts import render
from .models import Order

def index_page(request):
    objects_list = Order.objects.all()
    # return render(request, 'base.html', {'objects_list': objects_list})
    return render(request, 'ex_crm/index.html', {'objects_list': objects_list})
