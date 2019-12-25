from django.urls import path

from . import views

urlpatterns = [
    path('', views.index2, name='index2'),
    path('2/', views.index, name='index'),
    path('json_reco/', views.recommend_json),
    path('book_list/', views.get_book_list),
    path('saveLog/',views.saveLog)
]