from django.http import HttpResponse
from .models import Books
from django.template import loader
from django.shortcuts import render

# Create your views here.

def index(request):
    book_list = Books.objects.order_by('name')
    template = loader.get_template('book_reco/index.html')
    context = {
        'book_list':book_list,
    }
    return HttpResponse(template.render(context,request))

def detail(request, book_id):
    return HttpResponse("책 넘버 %s." % book_id)