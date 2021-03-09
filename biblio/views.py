from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Book, Auteur, Genre, Edition
from .form import UploadFileForm, SearchBookForm
import csv, io
import requests

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

@login_required(login_url="/admin")
def upload_file(request):

    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)

        if form.is_valid():

            csv_file = request.FILES['file']
            data_set = csv_file.read().decode('UTF-8')
            io_string = io.StringIO(data_set)
            next(io_string)

            books_list= []
            for row in csv.reader(io_string, delimiter=';', quotechar='"'):
                
                edition = Edition.objects.create(nom='Gallimard')
                genre = Genre.objects.create(nom=row[5])
                auteurs = Auteur.objects.create(nom=row[3],prenom="John")

                book = Book.objects.create(nom=row[0],resume=row[1],ISBN=row[2],edition=edition,image_url=row[6])
                if book:
                    book.genres.add(genre)
                    book.auteurs.add(auteurs)
                
                books_list.append(book)

            return render(request, "biblio/csv.html", {"result": True, 'books': books_list})
    else:
        form = UploadFileForm()
    return render(request, 'biblio/csv2.html', {'form': form})
    

def api_search(request):

    url = 'https://www.googleapis.com/books/v1/volumes?'

    if request.method == 'POST':
        form = SearchBookForm(request.POST)

        if form.is_valid():
            result = form.cleaned_data['title']
            params = dict(q=result)

            resp = requests.get(url=url, params=params)
            data = resp.json()
            # book_data = data['items'][0]['volumeInfo']
            # title = book_data['title']
            # authors = 
            return render(request, 'biblio/api_search.html', {'form':form, 'data':data})

    else:
        form = SearchBookForm()
    return render(request, 'biblio/api_search.html', {'form': form})

    