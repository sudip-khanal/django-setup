from django.contrib import admin

from apps.book.models import Author, Book, Category

# Register your models here.


class BookAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "isbn", "publication_date"]
    search_fields = ["title", "author__full_name", "isbn"]
    list_filter = ["author", "categories"]


class AuthorAdmin(admin.ModelAdmin):
    list_display = ["full_name", "email", "phone"]
    search_fields = ["full_name", "email", "phone"]


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]


admin.site.register(Book, BookAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Author, AuthorAdmin)
