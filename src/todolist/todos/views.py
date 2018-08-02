from django.shortcuts import render,redirect
from .models import *
from .forms import Todo_Form, LoginForm , RegisterForm
from .models import Todo
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate , login





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

User = get_user_model()
def register(r):
    reg_form = RegisterForm(r.POST or None)
    context = {
        'registerform':reg_form
    }
    if reg_form.is_valid():
        username = reg_form.cleaned_data.get('username')
        email = reg_form.cleaned_data.get('email')
        password = reg_form.cleaned_data.get('password')
        new_user = User.objects.create_user(username,email,password)

    return render(r,'auth/register.html',context)


def login_page(r):
    login_form = LoginForm(r.POST or None)
    context = {
        'login_form':login_form
    }
    print('User Logged in :')
    print(r.user.is_authenticated)
    if login_form.is_valid():
        print(login_form.cleaned_data)
        username = login_form.cleaned_data.get('username')
        password = login_form.cleaned_data.get('password')
        user = authenticate(r,username=username,password=password)
        print("User Logged in:")
        print(r.user.is_authenticated)
        print(user)
        if user is not None:
            print(r.user.is_authenticated)
            login(r,user)
            # login_form['login_form']=login_form
            return redirect('/todos/')
        else:
            print('Error')


    return render(r,'auth/login.html',context)