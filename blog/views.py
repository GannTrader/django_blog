from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
	posts = Post.objects.all()
	return render(request, 'index.html', {'posts': posts})

def detail(request, id):
	post = Post.objects.get(id = id)
	return render(request, 'detail.html', {'post':post})

def loginUser(request):
	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(request, username = username, password = password)

	if user is not None:
		login(request, user)
	return redirect('blog:index')

def logoutUser(request):
	logout(request)
	return redirect('blog:index')