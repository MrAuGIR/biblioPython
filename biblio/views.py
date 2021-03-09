from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Book, Auteur, Genre, Edition
import csv

# Create your views here.

def index(request):
    book_list = Book.objects.all()
    context = {'book_list': book_list}
    return render(request, 'biblio/index.html', context)

def detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'biblio/detail.html', {'book':book})

def authors(request):
    authors = Auteur.objects.all()
    return render(request, 'biblio/authors.html', {'authors':authors})

def author_detail(request,id):
    author = get_object_or_404(Auteur, pk=id)
    return render(request, 'biblio/author_detail.html', {'author':author})

def genres(request):
    genres = Genre.objects.all()
    return render(request, 'biblio/genres.html', {'genres':genres})

def genre_detail(request,id):
    genre = get_object_or_404(Genre, pk=id)
    return render(request, 'biblio/genre_detail.html', {'genre':genre})

def editions(request):
    editions = Edition.objects.all()
    return render(request, 'biblio/editions.html', {'editions':editions})

def edition_detail(request,id):
    edition = get_object_or_404(Edition, pk=id)
    return render(request, 'biblio/edition_detail.html', {'edition':edition})

def imports(request):
    if request.method == 'POST':
        file = request.POST
    return render(request, 'biblio/imports.html', {'imports':imports} )
