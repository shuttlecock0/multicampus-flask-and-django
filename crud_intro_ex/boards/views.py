from django.shortcuts import render, redirect
from .models import Board
# Create your views here.
def index(request):
    boards = Board.objects.all()
    context = {'boards': boards}
    return render(request, 'boards/index.html', context)

def new(request):
    return render(request, 'boards/new.html')

def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    board = Board(title=title, content=content)
    board.save()
    return redirect('/boards/')

def delete(request, pk):
    board = Board.objects.get(pk=pk)
    board.delete(pk=pk)
    return redirect('/boards/')
