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
    image_file = models.ImageField(blank=True, null=True)
    image_url = models.URLField(blank=True, null=True)
    resume = models.TextField()
    ISBN = models.CharField(max_length=13)


    @property
    def image(self):
        img = self.image_url
        if self.image_file:
            img = self.image_file.url
        return img






