from django.shortcuts import render
from django.views import View
# Create your views here.


class CustomersView(View):
    """
    Description: Model Description
    """
    template_name = 'accounts/customer.html'

    def get(self, request, *args, **kwargs):
        context = {
            'form':'form'
        }
        return render(request, self.template_name)


class HomeView(View):
    """
    Description: Model Description
    """
    template_name = 'accounts/dashboard.html'

    def get(self, request, *args, **kwargs):
        context = {

            'form':'form'
        }
        return render(request, self.template_name)


class ProductView(View):
    """
    Description: Model Description
    """
    template_name = 'accounts/products.html'

    def get(self, request, *args, **kwargs):
        context = {
        
            'form':'form'
        }
        return render(request, self.template_name)
