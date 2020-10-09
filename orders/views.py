from django.shortcuts import render
from django.views.generic.base import TemplateView
# Create your views here.

class Orderpageview(TemplateView):
    template_name = 'orders/purchase.html'
