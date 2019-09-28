from django.urls import path

from . import views

urlpatterns = [
    path('', views.index2, name='index2'),
    path('2/', views.index, name='index'),
    path('<int:book_id>/', views.recommend, name='recommend'),
    path('<int:book_id>/json/', views.recommend_json, name='recommend'),
]