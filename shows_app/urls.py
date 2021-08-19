from django.urls import path
from . import views

urlpatterns = [
    path('', views.base),
    path('shows', views.index),
    # path('new' , views.new),
]
