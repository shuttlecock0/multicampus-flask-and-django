from django.shortcuts import render, redirect
from .models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'post/index.html', context)

def new(request):
    return render(request, 'post/new.html')

def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    post = Post(title=title, content=content)
    post.save()
    return redirect(f'/post/{post.pk}/')

def detail(request, pk):
    post = Post.objects.get(pk=pk)
    context = {'post': post}
    return render(request, 'post/detail.html', context)
