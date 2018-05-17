from django.shortcuts import render, get_object_or_404, redirect
from .models import Todo

from .forms import TodoModelForm

# Create your views here.
def index(request):
    todos = Todo.objects.all()
    return render(request, 'todo/index.html', {'todos': todos})

def new(request):
    form = TodoModelForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('todo:index')
    return render(request,'todo/new.html',{
        'form':form
    })

def show(request, pk):
    # post = Post.objects.get(pk = pk)
    todo = get_object_or_404(Todo,pk=pk)
    return render(request,'todo/show.html',{'todo':todo})

def edit(request, pk):
    todo = get_object_or_404(Todo,pk=pk)
    form = TodoModelForm(request.POST or None,instance=todo)
    if form.is_valid():
        form.save()
        return redirect('todo:index')
    return render(request,'todo/edit.html',{
        'form':form
    })

def delete(request, pk):
    todo = get_object_or_404(Todo,pk=pk)
    todo.delete()
    return redirect('todo:index')
