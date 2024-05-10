from django.shortcuts import render, redirect
from .models import *

# Create your views here.

def todo(request):
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        
        todo = to_do(title=title, description=description)
        todo.save()
        
        
    todo_list = to_do.objects.all()
    
    context = {
        'TD':todo_list
    }
    
    return render (request, 'index.html',context)


def delete_todo(request,pk):
    todo = to_do.objects.get(id=pk)
    todo.delete()
    
    return redirect ('todo')