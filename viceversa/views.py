from django.http import HttpResponse
from django.shortcuts import render
def about(request):
	return HttpResponse('This is about pagen')


def home(request):
	return render(request, 'home.html')
