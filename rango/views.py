from rango.models import Page
from django.http import HttpResponse
from django.shortcuts import render
from rango.models import Category

def index(request):
 #   context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}
  #  return render ( request, 'rango/index.html', context=context_dict )
    category_list = Category.objects.order_by('-likes')[:5]
    pages = Page.objects.order_by ( '-views' )[:5]
    context_dict = {'categories': category_list, 'pages': pages}
    return render ( request, 'rango/index.html', context_dict )
    return HttpResponse ( 'Rango says hey there partner! <br/> <a href=' / rango / about / '>About</a>.')

def about(request):
    context_dict = {'boldmessage': "This tutorial has been put together by Muhammad Ikhwani"}
    return render ( request, 'rango/about.html', context=context_dict )
    return HttpResponse('Rango says here is the about page. <a href="/rango/">Index</a>.' )

def show_category(request, category_name_slug):
    context_dict = {}
    try:
        category = Category.objects.get ( slug=category_name_slug )
        pages = Page.objects.filter ( category=category )
        context_dict['pages'] = pages
        context_dict['category'] = category
    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['pages'] = None

    return render ( request, 'rango/category.html', context_dict )
