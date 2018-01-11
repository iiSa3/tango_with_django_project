from django.shortcuts import render

from django.http import HttpResponse

def index(request):
	return HttpResponse("Rango says hey there partner! <a href='/rango/about/'>about page</a>")


def about(request):
	return HttpResponse("Here is the about page.")