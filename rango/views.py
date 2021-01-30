from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from rango.models import Category, Page


def index(request):
    category_list = Category.objects.order_by('-likes')[:5]

    context_dict = {}
    context_dict['boldmessage'] = 'Crunchy, creamy, cookie, candy, cupcake!'
    context_dict['categories'] = category_list

    # The code for displaying the top viewd pages without using order_by is this:
    # pages = [page for page in sorted(Page.objects.all(), key= lambda x: x.views, reverse=True)[:5]]

    pages = Page.objects.order_by('-views')[:5]
    context_dict['pages'] = pages

    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    context_dict = {'MEDIA_URL' : settings.MEDIA_URL}
    return render(request, 'rango/about.html', context=context_dict)

def show_category(request, category_name_slug):

    context_dict = {}

    try:
        category = Category.objects.get(slug=category_name_slug)
        pages = Page.objects.filter(category=category)

        context_dict['category'] = category
        context_dict['pages'] = pages

    except Category.DoesNotExist:

        context_dict['category'] = None
        context_dict['pages'] = None



    return render(request, 'rango/category.html', context=context_dict)

    
