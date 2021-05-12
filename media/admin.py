from django.contrib import admin
from .models import OtherItem
from .models import Movie
from .models import Book
from .models import Copy_of_book
from .models import Copy_of_Movies
from .models import Copy_of_Other
from .models import is_borrowing_book
from .models import is_borrowing_movie
from .models import is_borrowing_other
from .models import book_is_of
from .models import movie_is_of
from .models import other_is_of
from .models import has_borrowed_book
from .models import has_borrowed_movie
from .models import has_borrowed_other
from .models import Written_by
from .models import Branch
from .models import Genre
from .models import Collection
from .models import Author
from .models import Publisher
from .models import Staff
from .models import Manager

class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publisher", "collection", "genre")

class MovieAdmin(admin.ModelAdmin):
    list_display = ("title", "rating", "length", "director", "collection", "genre")

class OtherAdmin(admin.ModelAdmin):
    list_display = ("title", "type", "creator", "collection", "genre")

class CBookAdmin(admin.ModelAdmin):
    list_display = ("item", "copy_no", "copy_condition")

class COtherAdmin(admin.ModelAdmin):
    list_display = ("item", "copy_no", "copy_condition")

class CMovieAdmin(admin.ModelAdmin):
    list_display = ("item", "copy_no", "copy_condition")

class CMovieAdmin(admin.ModelAdmin):
    list_display = ("item", "copy_no", "copy_condition")

class isBBookAdmin(admin.ModelAdmin):
    list_display = ("user", "book", "copy_no", "checkout_date", "due_date")

class isBMovieAdmin(admin.ModelAdmin):
    list_display = ("user", "movie", "copy_no", "checkout_date", "due_date")

class isBOtherAdmin(admin.ModelAdmin):
    list_display = ("user", "otherItem", "copy_no", "checkout_date", "due_date")

class hasBBookAdmin(admin.ModelAdmin):
    list_display = ("user", "book", "copy_no", "checkout_date", "date_returned", "condition_before", "condition_after", "late_return_fee")

class hasBMovieAdmin(admin.ModelAdmin):
    list_display = ("user", "movie", "copy_no", "checkout_date", "date_returned", "condition_before", "condition_after", "late_return_fee")

class hasBOtherAdmin(admin.ModelAdmin):
    list_display = ("user", "otherItem", "copy_no", "checkout_date", "date_returned", "condition_before", "condition_after", "late_return_fee")

class BookIsOfAdmin(admin.ModelAdmin):
    list_display = ("item", "genre")

class MovieIsOfAdmin(admin.ModelAdmin):
    list_display = ("item", "genre")

class OtherIsOfAdmin(admin.ModelAdmin):
    list_display = ("item", "genre")

class Written_byAdmin(admin.ModelAdmin):
    list_display = ("book", "author")

class BranchAdmin(admin.ModelAdmin):
    list_display = ("name", "location")

class GenreAdmin(admin.ModelAdmin):
    list_display = ("name", "demographic")

class CollectionAdmin(admin.ModelAdmin):
    list_display = ("name", "year")

class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name", "location")

class PublisherAdmin(admin.ModelAdmin):
    list_display = ("name", "location")

class StaffAdmin(admin.ModelAdmin):
    list_display = ("name", "salary")

class ManagerAdmin(admin.ModelAdmin):
    list_display = ("nationality", "favoriteFood")

admin.site.register(OtherItem, OtherAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Copy_of_book, CBookAdmin)
admin.site.register(Copy_of_Movies, CMovieAdmin)
admin.site.register(Copy_of_Other, COtherAdmin)
admin.site.register(is_borrowing_book, isBBookAdmin)
admin.site.register(is_borrowing_movie, isBMovieAdmin)
admin.site.register(is_borrowing_other, isBOtherAdmin)
admin.site.register(has_borrowed_book, hasBBookAdmin)
admin.site.register(has_borrowed_movie, hasBMovieAdmin)
admin.site.register(has_borrowed_other, hasBOtherAdmin)
admin.site.register(book_is_of, BookIsOfAdmin)
admin.site.register(movie_is_of, MovieIsOfAdmin)
admin.site.register(other_is_of, OtherIsOfAdmin)
admin.site.register(Written_by, Written_byAdmin)
admin.site.register(Branch, BranchAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Collection, CollectionAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Staff, StaffAdmin)
admin.site.register(Manager, ManagerAdmin)


