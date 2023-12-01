from django.urls import path
from .views import *
from . import views
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('', views.index, name='index'),
    path('login/',login.as_view(), name='login'),
    path('logout/',LogoutView.as_view(next_page = 'login'), name = 'logout'),
    path('new/', views.newProduct, name='newproduct'),
    path('update/<int:id>', views.update, name='update-product'),
    path('sell/', views.sellProduct, name= 'sell-product'),
    path('item/<int:id>', views.sellItem, name= 'sell-item'),
    path('solled/', views.solledProduct, name='solled-item'),
    path('deleted/',views.Deleted, name = 'deleted-item'),
    path('about/', views.about, name='about'),
    path('delete/<int:id>', views.deleteItem, name= 'delete-item'),
    path('search/', views.search, name= 'search'),
]