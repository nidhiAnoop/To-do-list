
from django.shortcuts import render, redirect
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