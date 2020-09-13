from django.db import models

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length = 255)
	image = models.FileField()
	body = models.TextField()
	created_at = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return self.title

class Comment(models.Model):
	post = models.ForeignKey(Post, on_delete = models.CASCADE)
	username = models.CharField(max_length = 255)
	email = models.EmailField()
	comment = models.TextField()
	created_at = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return self.username