from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model


User = get_user_model()
def index(r):
    context = {}
    user = User.objects.all()
    if r.user.is_authenticated:
        print('User is Authenticated')
        context['username']=user[0].username

    else:
        print('No Authentication')
    return render(r,'index.html',context)


