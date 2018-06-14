from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Todo

from .forms import TodoModelForm, DeleteConfirmForm

# Create your views here.
def index(request):
    todos = Todo.objects.all()
    return render(request, 'todo/index.html', {'todos': todos})

@login_required
def new(request):
    form = TodoModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        todo = form.save(request.user)
        # todo.creator = request.user
        # todo.save()
        return redirect('todo:index')
    return render(request,'todo/new.html',{
        'form':form
    })

@login_required
def show(request, pk):
    # post = Post.objects.get(pk = pk)
    todo = get_object_or_404(Todo,pk=pk)
    return render(request,'todo/show.html',{'todo':todo})

@login_required
def edit(request, pk):
    todo = get_object_or_404(Todo,pk=pk)
    form = TodoModelForm(request.POST or None, request.FILES or None, instance=todo)
    if form.is_valid():
        todo = form.save(request.user)
        # todo.creator = request.user
        # todo.save()
        # form.save_m2m()
        return redirect('todo:index')
    return render(request,'todo/edit.html',{
        'form':form
    })

@login_required
def delete(request, pk):
    # todo = get_object_or_404(Todo,pk=pk)
    # todo.delete()
    # return redirect('todo:index')
    form = DeleteConfirmForm(request.POST or None)
    if form.is_valid() and form.cleaned_data['check']:
        todo = get_object_or_404(Todo,pk=pk)
        todo.delete()
        return redirect('todo:index')
    return render(request,'todo/delete.html', {'form': form})
