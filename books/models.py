from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=120)
    subtitle = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    bio = models.TextField(blank=True, null=True)
    author_id = models.ForeignKey("Author", on_delete=models.CASCADE)


    def __str__(self):
        return self.title

class Author(models.Model):
    ismi = models.CharField(max_length=120)
    fam = models.CharField(max_length=200)
    adress = models.CharField(max_length=400)

    def __str__(self):
        return self.ismi