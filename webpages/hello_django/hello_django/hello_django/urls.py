"""hello_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include,path
#from covid_blog import views
from social_app import views

urlpatterns = [
	
	#path('covid-blog/', views.index,name='index'),
    path('admin/', admin.site.urls),
    
    #path ('', views.index,name='index'),
    #path('covid-blog/<int:article_id>/',views.detail,name='detail'),

    path('social_app/', views.social,name='social'),
    path('social_app/users/', views.ShowUsers,name='ShowUsers'),
    path('social_app/groups/', views.ShowGroups,name='ShowGroups'),
    path('social_app/events/', views.ShowEvents,name='ShowEvents'),

    path('social_app/users/<str:first_name>/',views.UserDetail,name='UserDetail'),
    path('social_app/groups/<str:name>/',views.GroupDetail,name='GroupDetail'),
    path('social_app/events/<str:event_title>/',views.EventDetail,name='EventDetail'),
]
