from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def Jampandu(request):
    return HttpResponse('<h1><marquee>hi jampandu how are u</h1></marquee>')

def Jigelrani(request):
    return HttpResponse('<h1><marquee> iam fine</h1></marquee>')

