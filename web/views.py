from django.shortcuts import render
from django.http import HttpResponse
from pymongo import MongoClient

MONGO_URI = "mongodb://root:servicio@mongo:27017?retryWrites=true&w=majority"

def connect():
    client = pymongo.MongoClient(MONGO_URI)
    db = client["servsoc"]
    collection = db["estudiantes"]

def registro(request):
    return render(request,"registro.html")


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
