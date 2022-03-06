from itertools import product
from django import http
from django.http import HttpResponse
from django.shortcuts import render
from .models import Product


def index(request):
    product = Product.objects.all()
    return render(request, 'index.html', {'product':product})
