from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='oindex'),
    path('<int:id>/', views.index, name='oindex'),
]
