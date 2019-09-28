from django.http import HttpResponse
from .models import Books
from .models import Cossim
from .models import Category
from django.template import loader
from django.template.context_processors import csrf
from django.core import serializers
from django.shortcuts import render

# Create your views here.


def index2(request):
    book_list = Books.objects.order_by('name')
    template = loader.get_template('book_reco/index1.html')
    context = {
        'book_list':book_list,
    }
    return HttpResponse(template.render(context,request))


def index(request):
    book_list = Books.objects.order_by('name')
    template = loader.get_template('book_reco/index.html')
    context = {
        'book_list':book_list,
    }
    return HttpResponse(template.render(context,request))


def recommend(request, book_id):
    c = {}
    c.update(csrf(request))
    book = Books.objects.filter(book_id=book_id)[0]
    cosim_list = Cossim.objects\
            .select_related('book') \
            .filter(book=book_id) \
            .order_by('-sim')[:10]
    template = loader.get_template('book_reco/reco.html')
    context = {
        'cosim_list': cosim_list,
        'book':book,
    }

    return HttpResponse(template.render(context,request))

def recommend_json(request, book_id):
    book = Books.objects.filter(book_id=book_id)[0]
    cosim_list = Cossim.objects\
            .select_related('book') \
            .filter(book=book_id) \
            .order_by('-sim')[:10]
    json_str ="["
    json_str += "{"
    json_str += ("\"name\": \"" + book.name + "\",")
    json_str += ("\"author\": \"" + book.author + "\",")
    json_str += ("\"url\": \"" + book.url + "\"")
    json_str += "},"
    for i in cosim_list:
        json_str += "{"
        json_str += ("\"name\": \""+i.book_id1.name+"\",")
        json_str += ("\"author\": \"" + i.book_id1.author + "\",")
        json_str += ("\"publish\": \"" + i.book_id1.publish + "\",")
        json_str += ("\"url\": \"" + i.book_id1.url + "\",")
        json_str += ("\"sim\": " + str(i.sim) + ",")
        json_str += ("\"women10\": " + str(i.book_id1.women10) + ",")
        json_str += ("\"women20\": " + str(i.book_id1.women20) + ",")
        json_str += ("\"women30\": " + str(i.book_id1.women30) + ",")
        json_str += ("\"women40\": " + str(i.book_id1.women40) + ",")
        json_str += ("\"women50\": " + str(i.book_id1.women50) + ",")
        json_str += ("\"women60\": " + str(i.book_id1.women60) + ",")
        json_str += ("\"men10\": " + str(i.book_id1.men10) + ",")
        json_str += ("\"men20\": " + str(i.book_id1.men20) + ",")
        json_str += ("\"men30\": " + str(i.book_id1.men30) + ",")
        json_str += ("\"men40\": " + str(i.book_id1.men40) + ",")
        json_str += ("\"men50\": " + str(i.book_id1.men50) + ",")
        json_str += ("\"men60\": " + str(i.book_id1.men60))
        json_str += "},"
    json_str = json_str[:-1]+"]"
    return HttpResponse(json_str,content_type=u"application/json; charset=utf-8")
