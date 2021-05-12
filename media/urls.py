
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Userhome, name='home'),
    path('books/', views.Books, name ='books'),
    path('movies/', views.Movies, name = 'movies'),
    path('otheritems/', views.Otheritems, name = 'otheritems'),
    path('view/', views.view, name = 'view'),
    path('borrow/<int:pk>', views.borrow, name = 'borrow'),
    path('return/<int:pk>', views.returnbook, name = 'returnBook'),
]