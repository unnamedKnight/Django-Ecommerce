from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Product
from category.models import Category

# Create your views here.


def home(request):
    '''
    This view is the home page for greatkart project.
    '''
    
    products = Product.objects.filter(is_available=True)
    
    context = {
        "products": products
    }
    
    return render(request, 'store/home.html', context)


def store(request, category_slug=None):
    
    if category_slug is None:
        products = Product.objects.filter(is_available=True)
    else:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category)
    
    
    context = {
        "products": products
    }
    
    return render(request, 'store/store.html', context)