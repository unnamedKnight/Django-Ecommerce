from multiprocessing import context
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Product
from category.models import Category

# Create your views here.


def home(request):
    """
    This view is the home page for greatkart project.
    """

    products = Product.objects.filter(is_available=True)
    categories = Category.objects.all()

    context = {
        "products": products,
        "categories": categories,
    }

    return render(request, "store/home.html", context)


def store(request, category_slug=None):

    if category_slug is None:
        products = Product.objects.filter(is_available=True)
    else:
        # By using the get_object_or_404
        # if the object is not found an 404 error will raised automatically
        # we dont need to define other condition  to handle the error

        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category, is_available=True)

    categories = Category.objects.all()

    context = {
        "products": products,
        "categories": categories,
    }

    return render(request, "store/store.html", context)


def product_detail(request, category_slug, product_slug):
    """
    This a prodict detail view of a product.
    """
    product = Product.objects.get(slug=product_slug)
    categories = Category.objects.all()

    context = {"product": product,
               "categories": categories,}

    return render(request, "store/product-detail.html", context)
