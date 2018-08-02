from django.shortcuts import render,redirect


def index(r):
    return render(r,'index.html')


