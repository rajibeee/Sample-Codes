from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.urls import path
from django.shortcuts import render
from .models import UserProfile
from .models import Group
from .models import Event

import sys
from subprocess import run,PIPE
# Create your views here.
def social(request):
	#return HttpResponse("Hello, world! 😎")
	return render(request,'social_app/index.html')
	
	
def ShowUsers(request):
	user_list= UserProfile.objects.order_by('-first_name')
	template=loader.get_template('social_app/users.html')
	context={
		'user_list':user_list,
	}
	
	return HttpResponse(template.render(context,request))
	
def ShowGroups(request):
	group_list= Group.objects.order_by('-name')
	template=loader.get_template('social_app/groups.html')
	context={
		'group_list':group_list,
	}
	
	return HttpResponse(template.render(context,request))



def ShowEvents(request):
	event_list= Event.objects.order_by('-event_title')
	template=loader.get_template('social_app/events.html')
	context={
		'event_list':event_list,
	}
	
	return HttpResponse(template.render(context,request))

def UserDetail(request, first_name):
	return HttpResponse("This is the page for %s" %first_name)

def GroupDetail(request, name):
	return HttpResponse("This is the Group page for %s" %name)

def EventDetail(request, event_title):
	return HttpResponse("This is the Event page for %s" %event_title)