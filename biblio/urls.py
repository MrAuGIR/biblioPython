from django.urls import path

from . import views

app_name = 'biblio'
urlpatterns = [
    # ex: /biblio/
    path('authors/<int:id>/', views.author_detail, name="author_detail"),
    path('genres/<int:id>/', views.genre_detail, name="genre_detail"),
    path('editions/<int:id>/', views.edition_detail, name="edition_detail"),
    path('', views.index, name='index'),
    path('<int:book_id>/', views.detail, name='detail'),
    path('authors/', views.authors, name="authors"),
    path('genres/', views.genres, name="genres"),
    path('editions/', views.editions, name="editions"),
    path('imports/',views.imports, name="imports")
    
]
