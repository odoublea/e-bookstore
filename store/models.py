from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=150, unique=True, db_index=True)
    icon = models.FileField()
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=150, unique=True, db_index=True)
    bio = models.TextField()
    pic = models.FileField()
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, db_index=True)
    price = models.IntegerField()
    stock = models.IntegerField()
    coverpage = models.FileField()
    bookpage = models.FileField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    totalreview = models.IntegerField(default=1)
    totalrating = models.IntegerField(default=5)
    status = models.IntegerField(default=0)
    description = models.TextField()

    def __str__(self):
        return self.name


class Review(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    review_star = models.IntegerField()
    review_text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)


class Slider(models.Model):
    title = models.CharField(max_length=150)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slideimg = models.FileField()

    def __str__(self):
        return self.title

