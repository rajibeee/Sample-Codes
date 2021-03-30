from django.db import models

class UserProfile(models.Model):
	about_me=models.TextField()
	birth_date=models.DateTimeField()
	fav_movies=models.CharField(max_length=100)
	first_name=models.CharField(max_length=30)
	last_name=models.CharField(max_length=30)
	username=models.CharField(max_length=20)
	photo_url=models.URLField()


class Group(models.Model):

	name=models.CharField(max_length=100)
	members=models.TextField() #not sure
	description=models.TextField()
	category=models.TextField() #not sure
	website_url=models.URLField()

class Event(models.Model):
	creator_name=models.CharField(max_length=100)
	description=models.TextField()
	start_time=models.DateTimeField()
	end_time=models.DateTimeField()
	location=models.CharField(max_length=100)
	event_title=models.CharField(max_length=500)


class Feed(models.Model):
	FEED=[('P','Photo'),('V','Video'),('T','Text')] #custom Feed type
	feed_type=models.CharField(max_length=1,choices=FEED)
	total_likes=models.IntegerField(null=True)
	comments=models.CharField(max_length=100)
	content=models.TextField() #not sure
