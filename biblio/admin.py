from django.contrib import admin
from .models import Book, Auteur, Genre, Edition
# Register your models here.

admin.site.register(Book)
admin.site.register(Auteur)
admin.site.register(Genre)
admin.site.register(Edition)

