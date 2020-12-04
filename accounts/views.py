from django.shortcuts import render
from django.http import HttpResponse

from .models import *


def home(request):
    customers = Customer.objects.all()
    orders = Order.objects.all()
    total_customers = customers.count()
    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()
    
    context = {
        'customers': customers,
        'orders': orders,
        'total_customers': total_customers,
        'total_orders': total_orders,
        'delivered': delivered,
        'pending': pending,
    }

    return render(request, 'accounts/dashboard.html', context)

def products(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'accounts/products.html', context)

def customer(request, pk_test):
    customers = Customer.objects.get(id=pk_test)
    orders = customers.order_set.all()
    order_count = orders.count()

    context = {
        'customer': customers,
        'orders': orders,
        'order_count': order_count,
    }
    return render(request, 'accounts/customer.html', context)