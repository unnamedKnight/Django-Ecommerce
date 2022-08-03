from django.shortcuts import render
from category.models import Category
# Create your views here.


def cart(request):
    
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    
    return render(request, "carts/cart.html", context)
