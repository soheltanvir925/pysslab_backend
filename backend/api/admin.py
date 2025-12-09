from django.contrib import admin
from .models import CustomUser, Student, Author, Book

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Student)
admin.site.register(Author)
admin.site.register(Book)