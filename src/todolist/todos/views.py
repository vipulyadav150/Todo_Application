from django.shortcuts import render,redirect
from .models import *
from .forms import Todo_Form
from .models import Todo

def home_page(r):
    todos_fetch = Todo.objects.all()

    context = {
        'title':'TODO',
        'todos': todos_fetch
    }
    return render(r,'todos/home.html',context)




def todo_details(r,id):
    particular_todo = Todo.objects.get(id=id)
    context = {
        'todos_specific':particular_todo
    }
    print(particular_todo)
    return render(r,'todos/todo_details.html',context)



def add_todos(r):
    todo_form = Todo_Form(r.POST or None)

    context = {
        'form':todo_form
    }

    if todo_form.is_valid():
        print(todo_form.cleaned_data)

        #Create a new object to add it to default model
        todo = Todo(title=todo_form.cleaned_data.get('task_title'),
                    text=todo_form.cleaned_data.get('task_description'))
        todo.save()
        return redirect('/todos/add/')

    return render(r,'todos/add_todo.html',context)