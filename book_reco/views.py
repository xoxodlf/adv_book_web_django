from django.http import HttpResponse, JsonResponse
from .models import *
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.shortcuts import render
from datetime import datetime
from django.db import connections
# Create your views here.


def index2(request):
    request.session.create()
    UserTime.objects.create(session_id = request.session.session_key,in_field=datetime.now(),last_action=datetime.now())
    book_list = Books.objects.filter(category_id=1).order_by('name')
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

def saveLog(request):
    UserAction.objects.create(session_id=request.session.session_key,user_action='click',time=datetime.now(),category=request.POST.get('category_id'),book_no=request.POST.get('book_id'))
    ut=UserTime.objects.get(session_id = request.session.session_key)
    ut.last_action=datetime.now()
    ut.save()
    context = {
        'msg':'success'
    }
    return JsonResponse(context)

@csrf_exempt
def get_book_list(request):
    category_id = request.POST.get('category_id')
    book_list = Books.objects.filter(category_id=category_id)
    books = []
    for bb in book_list:
        book = {'name' : bb.name, 'book_id' : bb.book_id}
        books.append(book)
    context = {
        'books' : books
    }
    return JsonResponse(context)

def recommend_json(request):
    book_id = request.POST.get('book_id')
    category_id = int(request.POST.get('category_id'))
    ut=UserTime.objects.get(session_id = request.session.session_key)
    ut.last_action=datetime.now()
    ut.save()
    UserAction.objects.create(session_id=request.session.session_key, user_action='reco', time=datetime.now(), category=category_id, book_no=book_id)
    book = Books.objects.filter(book_id=book_id)[0]
    cosim_list=[]
    if category_id==1:
        cosim_list = Cossim.objects\
            .select_related('book') \
            .filter(book=book_id) \
            .order_by('-sim')[:10]
    elif category_id==2:
        cosim_list = Cossim2.objects\
            .select_related('book') \
            .filter(book=book_id) \
            .order_by('-sim')[:10]
    elif category_id==3:
        cosim_list = Cossim3.objects\
            .select_related('book') \
            .filter(book=book_id) \
            .order_by('-sim')[:10]
    elif category_id==4:
        cosim_list = Cossim4.objects\
            .select_related('book') \
            .filter(book=book_id) \
            .order_by('-sim')[:10]
    elif category_id==5:
        cosim_list = Cossim5.objects\
            .select_related('book') \
            .filter(book=book_id) \
            .order_by('-sim')[:10]
    elif category_id==6:
        cosim_list = Cossim6.objects\
            .select_related('book') \
            .filter(book=book_id) \
            .order_by('-sim')[:10]
    elif category_id==7:
        cosim_list = Cossim7.objects\
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
        json_str += ("\"category\": \"" + str(i.book_id1.category.category_id) + "\",")
        json_str += ("\"book_id\": \"" + str(i.book_id1.book_id) + "\",")
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


