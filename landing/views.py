from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError
from .models import *
from products.models import *
from django.utils import translation

def home(request):

    category = ProductCategory.objects.filter(is_active=True)
    product_item = Product.objects.filter(is_active=True)

    if translation.LANGUAGE_SESSION_KEY in request.session:
        del request.session[translation.LANGUAGE_SESSION_KEY]

    return render(request, 'landing/home.html', locals())

def categories(request, category_id):
    category = ProductCategory.objects.filter(is_active=True)
    products = Product.objects.filter(category=category_id,is_active=True)

    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()

    print(request.session.session_key)

    return render(request, 'landing/category.html', locals())


def categoriespage(request):

    category = ProductCategory.objects.filter(is_active=True)
    product_item = Product.objects.filter(is_active=True)

    if translation.LANGUAGE_SESSION_KEY in request.session:
        del request.session[translation.LANGUAGE_SESSION_KEY]

    return render(request, 'landing/categories.html', locals())


