from django.contrib import admin
from .models import Author, Book, Category, Slider

admin.site.site_header="Welcome To The Bookstore"

@admin.register(Category)
class AddCategory(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Author)
class AddAuthor(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Book)
class AddBook(admin.ModelAdmin):
    list_display = ['title', 'price', 'stock', 'status', 'created', 'updated']
    list_filter = ['status', 'created', 'updated']
    list_editable = ['price', 'status']
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Slider)
class AddSlider(admin.ModelAdmin):
    list_display = ['title', 'created', 'updated']
