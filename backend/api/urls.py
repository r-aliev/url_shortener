from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_urls, name="get_urls"),
    path('add/', views.add_url, name="add_url"),
    path('<str:slug>', views.redirect_to_url, name="redirect_to_url"),
]
