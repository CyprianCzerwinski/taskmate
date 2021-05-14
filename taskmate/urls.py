
from django.contrib import admin
from django.urls import path, include, re_path
from todolist_app import views as todolist_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', todolist_views.index, name='index'),
    path('todolist/', include('todolist_app.urls')),
    path('contact/', todolist_views.contact, name='contact'),
    path('about/', todolist_views.about, name='about'),
    path('files/', todolist_views.files, name='files'),
    path('portfolio/', todolist_views.portfolio, name='portfolio'),
    path('register/', todolist_views.registerPage, name='register'),
    path('login/', todolist_views.loginPage, name='login'),
    path('logout/', todolist_views.logoutUser, name='logout'),



]
