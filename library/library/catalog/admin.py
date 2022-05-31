from django.contrib import admin
from .models import BookInstance, Genre, Language, Author,Book

# Register your models here.
admin.site.register(Genre)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Language)
admin.site.register(BookInstance)
