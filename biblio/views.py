from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Book, Auteur, Genre, Edition

# Create your views here.

def index(request):
    book_list = Book.objects.all()
    context = {'book_list': book_list}
    return render(request, 'biblio/index.html', context)

def detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'biblio/detail.html', {'book':book})
