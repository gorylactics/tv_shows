from django.urls import path
from . import views

urlpatterns = [
    path('', views.base),
    path('shows/', views.index),
    path('shows/new' , views.new),
    path('shows/<int:id>' , views.shows),
    path('shows/<int:id>/edit', views.edit),
    path('shows/<int:id>/delete', views.delete)

]
