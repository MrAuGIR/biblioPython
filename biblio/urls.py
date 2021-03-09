from django.urls import path

from . import views

app_name = 'biblio'
urlpatterns = [
    # ex: /biblio/
    path('authors/<int:id>/', views.author_detail, name="author_detail"),
    path('', views.index, name='index'),
    path('<int:book_id>/', views.detail, name='detail'),
    path('authors/', views.authors, name="authors"),
    
]
