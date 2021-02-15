from django.urls import path
from todolist_app import views

urlpatterns = [
path('todolist/', views.todolist, name='todolist'),
path('contact/', views.contact, name='contact'),
path('about/', views.about, name='about'),
]
