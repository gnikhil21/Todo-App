from django.shortcuts import render,redirect
from .models import todoform
from django.http import HttpResponse
from .forms import TaskForm
from django.contrib import messages
# Create your views here.
def home(request):
    #item_list = form.objects.all()#order_by("-date")
    points = todoform.objects.all()
    print("##")
    form = TaskForm()
    if request.method == "POST":
        print("###")
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/todo/')
    #form = TaskForm()
  
    page = {
             "forms" : form,
             #"points" : points,
             
           }
    return render(request, 'index.html', page)
    
def notes(request):
    points = todoform.objects.all()
    return render(request, 'notes.html',{'points':points})

def delete(request,id):
    points = todoform.objects.get(id=id)
    if points:
        points.delete()
    return redirect('/todo/notes/')

def update(request,id):
    task=todoform.objects.get(id=id)
    form=TaskForm(instance=task)
    if request.method=="POST":
        form=TaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect('/todo/notes/')
    return render(request,'update.html',{'form':form,'id':id})