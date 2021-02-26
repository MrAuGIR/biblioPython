from django.db import models

# Create your models here.

class Auteur(models.Model):
    nom = models.CharField(max_length=200)
    prenom = models.CharField(max_length=200)

    def __str__(self):
        return self.nom

class Genre(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom

class Edition(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom

class Book(models.Model):
    nom = models.CharField(max_length=100)
    auteurs = models.ManyToManyField(Auteur)
    genres = models.ManyToManyField(Genre)
    edition = models.ForeignKey(Edition, on_delete=models.DO_NOTHING)
    image = models.ImageField(upload_to='../media/image')
    resume = models.TextField()
    ISBN = models.CharField(max_length=13)






