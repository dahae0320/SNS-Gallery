from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Post
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
  posts = Post.objects.all().order_by('-pub_date')
  return render(request, 'index.html', {'posts': posts})


@login_required(login_url='login_view')
def post(request):
  if request.method == 'POST':
    post = Post()
    post.description = request.POST['description']
    post.image = request.FILES['image']
    post.author = request.user
    post.pub_date = timezone.datetime.now()
    post.save()
    return redirect('index')
  return render(request, 'post.html')


@login_required(login_url='login_view')
def post_update(request, post_id):
  if request.method == 'POST':
    edit_post = Post.objects.get(id=post_id)
    edit_post.description = request.POST['description']
    edit_post.image = request.FILES['image']
    edit_post.author = request.user
    edit_post.pub_date = timezone.datetime.now()
    edit_post.save()
    return redirect('index')
  else:
    edit_post = Post.objects.get(id=post_id)
    return render(request, 'post_update.html', {'edit': edit_post})


@login_required(login_url='login_view')
def post_delete(request, post_id):
  post = Post.objects.get(id=post_id)
  post.delete()
  return redirect('index')
