from django.urls import path
from app import views

urlpatterns = [ 
    path('todo/',views.todo,name='todo'),
    path('', views.todo, name='index'),
    path('todo/delete/<int:pk>', views.delete_todo,name='delete_todo'),
]
