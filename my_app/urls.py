from django.urls import path
from . import views

app_name = 'todo_list'
urlpatterns = [
    path('', views.home, name='home'),
    path('add', views.add_item, name='add'),
    path('todolist', views.list_page, name='todo'),
]