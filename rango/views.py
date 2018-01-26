from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}
    return render ( request, 'rango/index.html', context=context_dict )
    return HttpResponse('Rango says hey there partner! <br/> <a href='/rango/about/'>About</a>.')

def about(request):
    context_dict = {'boldmessage': "This tutorial has been put together by Muhammad Ikhwani"}
    return render ( request, 'rango/about.html', context=context_dict )
    return HttpResponse('Rango says here is the about page. <a href="/rango/">Index</a>.' )
