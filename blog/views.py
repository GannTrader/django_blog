from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post, Comment
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
	posts = Post.objects.all()
	return render(request, 'index.html', {'posts': posts})

def detail(request, id):
	post = Post.objects.get(id = id)
	comments = Comment.objects.filter(post=post, status="active").order_by('-created_at')
	return render(request, 'detail.html', {'post':post, 'comments':comments})

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

def commentUser(request):
	id = request.POST.get('id')
	cmt_user = request.POST.get('cmt_user')
	cmt_email = request.POST.get('cmt_email')
	cmt_body = request.POST.get('cmt_body')

	Comment.objects.create(
		post = Post.objects.get(id=id),
		username = cmt_user,
		email = cmt_email,
		comment = cmt_body
		)
	return redirect('blog:detail')

