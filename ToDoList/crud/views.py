
from django.shortcuts import render, redirect, get_object_or_404
from .models import TodoItem
from .forms import TodoForm

# Create your views here.
def todo_list(request):
    todos = TodoItem.objects.all()
    data = {
        "todos" : todos
    }
    return render(request, "todo_lists.html", data)

def add_todo(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("todo_list")
    else:
        form = TodoForm()
    data = {
        "form" : form
    }
    return render(request, "add_todo.html", data)

def update_todo(request, pk):
    todo = get_object_or_404(TodoItem, pk=pk)
    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo) 
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = TodoForm()
    data = {
        "form" : form,
        'todo': todo,
    }
    return render(request, "update_todo.html", data)

def delete_todo(request, pk):
    todo = get_object_or_404(TodoItem, pk=pk)
    todo.delete()
    return redirect('todo_list')