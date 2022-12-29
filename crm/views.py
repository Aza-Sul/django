from django.shortcuts import render

from cms.models import CmsSlider
from price.models import PriceCard, PriceTable
from .forms import OrderForm
from .models import Order


def index(request):
    form = OrderForm()
    slider_list = CmsSlider.objects.all()
    price_card = PriceCard.objects.all()
    price_table = PriceTable.objects.all()

    context = {'slider_list': slider_list, 'price_card': price_card, 'price_table': price_table, 'form': form}

    return render(request, 'index.html', context)


def thanks(request):
    name = request.POST.get('name')
    phone = request.POST.get('phone')
    element = Order(order_name=name, order_phone=phone)
    element.save()

    return render(request, 'thanks.html', {'name': name, 'phone': phone})
