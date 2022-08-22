from django.contrib import admin
from .models import Author, Book, Category, Slider


class AddCategory(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, AddCategory)


class AddAuthor(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Author, AddAuthor)


class AddBook(admin.ModelAdmin):
    list_display = ['name', 'price', 'stock', 'status', 'created', 'updated']
    list_filter = ['status', 'created', 'updated']
    list_editable = ['price', 'stock', 'status']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Book, AddBook)


class AddSlider(admin.ModelAdmin):
    list_display = ['title', 'created', 'updated']


admin.site.register(Slider, AddSlider)