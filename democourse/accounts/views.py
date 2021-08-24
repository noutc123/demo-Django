from django.shortcuts import render
from django.views import View
from .models import *
# Create your views here.


class CustomersView(View):
    """
    Description: Model Description
    """
    template_name = 'accounts/customer.html'

    def get(self, request, *args, **kwargs):
        oders = Order.objects.all()
        customer = Custumer.objects.all()
        print(oders, customer,'hello ')
        context = {
            'oders': oders,
            'customers': customer,

        }
        return render(request, self.template_name, context)


class HomeView(View):
    """
    Description: Model Description
    """
    template_name = 'accounts/dashboard.html'

    def get(self, request, *args, **kwargs):
        oders = Order.objects.all()
        customer = Custumer.objects.all()
        total_orders = oders.count()
        total_customers = customer.count()
        delivered = oders.filter(status='Delivred').count()
        pending = oders.filter(status='Pending').count()

        context = {
            'oders': oders,
            'customers': customer,
            'total_orders': total_orders,
            'total_customers': total_customers, 
            'delivered': delivered,     
            'pending': pending,

        }
        return render(request, self.template_name, context)


class ProductView(View):
    """
    Description: Model Description
    """
    template_name = 'accounts/products.html'

    def get(self, request, *args, **kwargs):
        products = Product.objects.all()
        context = {
        
            'products': products,
        }
        return render(request, self.template_name, context)
