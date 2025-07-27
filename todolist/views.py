from django.views.generic import ListView 
from django.views.generic.edit import UpdateView , DeleteView , CreateView 
from django.urls import reverse_lazy
from .models import Task 
from django.shortcuts import render 

class HomePage(ListView):
    template_name = 'home.html' 
    model = Task 
    context_object_name = 'Tasks'
    

class AddTask(CreateView):
    model = Task 
    fields = ['name' , 'is_done']
    template_name = 'todolist/add.html'
    success_url = reverse_lazy('home')

class DeleteTask(DeleteView):
    model = Task 
    template_name = 'todolist/delete.html' 
    success_url = reverse_lazy('home')
    context_object_name = 'task'

class UpdateTask(UpdateView):
    model = Task 
    template_name = 'todolist/add.html'  
    fields = ['name' , 'is_done']
    success_url = reverse_lazy('home')

def compeleted_tasks(request):
    compeletedTasks = Task.objects.filter(is_done=True)
    
    return render (request , 'todolist/result_page.html' , {
        "Tasks" : compeletedTasks 
    })


def pending_tasks(request):
    pendingTasks = Task.objects.filter(is_done=False)
    

    return render (request , 'todolist/result_page.html' , {
        "Tasks" : pendingTasks 
    })


