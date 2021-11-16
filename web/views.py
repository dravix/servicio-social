from django.shortcuts import render
from django.http import HttpResponse
from pymongo import MongoClient


def registro(request):
    return render(request,"registro.html")

def login(request):
    return render(request,"login.html")

def index(request):
    return render(request,"index.html")
