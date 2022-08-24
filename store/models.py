from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User
import uuid


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=150, unique=True, db_index=True)
    icon = models.FileField()
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Author(models.Model):
    id=models.CharField(primary_key=True,default=uuid.uuid4, editable=False, max_length=36)
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=150, unique=True, db_index=True)
    bio = models.TextField()
    pic = models.FileField()
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name='book', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, db_index=True)
    price = models.IntegerField()
    stock = models.IntegerField()
    coverpage = models.FileField()
    bookpage = models.FileField()
    status = models.IntegerField(default=0)
    description = models.TextField()
    totalreview = models.IntegerField(default=1)
    totalrating = models.IntegerField(default=5)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


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

