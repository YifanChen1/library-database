from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta

class Collection(models.Model):
    name = models.CharField(max_length=100)
    year = models.DateTimeField()
        
    def __str__(self):
	    return self.name

class Genre(models.Model):
    name = models.CharField(max_length=100)
    demographic = models.CharField(max_length=100)

    def __str__(self):
	    return self.name

class Author(models.Model):
    name = models.CharField(max_length = 100)
    location = models.CharField(max_length=100)
        
    def __str__(self):
	    return self.name

class Publisher(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    
    def __str__(self):
	    return self.name

class OtherItem(models.Model):
    type = models.CharField(max_length=100)
    creator = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    collection = models.ForeignKey(Collection, null=True, on_delete=models.SET_NULL)
    genre =  models.ForeignKey(Genre, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title

class Movie(models.Model):
    title = models.CharField(max_length=100)
    rating = models.CharField(max_length=100)
    length =  models.DurationField()
    director = models.CharField(max_length=100)
    collection = models.ForeignKey(Collection, null=True, on_delete=models.SET_NULL)
    genre =  models.ForeignKey(Genre, null=True, on_delete=models.SET_NULL)
    
    def __str__(self):
        return self.title

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, null=True, on_delete=models.SET_NULL)
    publisher = models.ForeignKey(Publisher, null=True, on_delete=models.SET_NULL)
    collection = models.ForeignKey(Collection, null=True, on_delete=models.SET_NULL)
    genre = models.ForeignKey(Genre, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title

class Staff(models.Model):
    name = models.CharField(max_length=100)
    salary = models.IntegerField()

    def __str__(self):
	    return self.name

class Manager(Staff):
    nationality = models.CharField(max_length=100)
    favoriteFood = models.CharField(max_length=100)

class Branch(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    manager = models.ForeignKey(Manager, null=True, on_delete=models.SET_NULL)    

    def __str__(self):
	    return self.name

class Copy_of_book(models.Model):
    item = models.ForeignKey(Book, on_delete=models.CASCADE)
    copy_no = models.IntegerField()
    copy_condition = models.CharField(max_length=500)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)

    def __str__(self):
	    return self.item
        
class Copy_of_Other(models.Model):
    item = models.ForeignKey(OtherItem, on_delete=models.CASCADE)
    copy_no = models.IntegerField()
    copy_condition = models.CharField(max_length=500)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)

    def __str__(self):
	    return self.item

class Copy_of_Movies(models.Model):
    item = models.ForeignKey(Movie, on_delete=models.CASCADE)
    copy_no = models.IntegerField()
    copy_condition = models.CharField(max_length=500)
    models.ForeignKey(Branch, on_delete=models.CASCADE)

    def __str__(self):
	    return self.item

    class Meta:
      verbose_name_plural = "Copy_of_Movies"

class is_borrowing_book(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    copy_no = models.IntegerField()
    checkout_date = models.DateTimeField(auto_now_add=True, blank=True)
    due_date = models.DateTimeField()

    class Meta:
      verbose_name_plural = "Currently Borrowing Book Relations"

class is_borrowing_movie(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    copy_no = models.IntegerField()
    checkout_date = models.DateTimeField(auto_now_add=True, blank=True)
    due_date = models.DateTimeField()

    class Meta:
      verbose_name_plural = "Currently Borrowing Movie Relations"

class is_borrowing_other(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    otherItem = models.ForeignKey(OtherItem, on_delete=models.CASCADE)
    copy_no = models.IntegerField()
    checkout_date = models.DateTimeField(auto_now_add=True, blank=True)
    due_date = models.DateTimeField()
    
    class Meta:
      verbose_name_plural = "Currently Borrowing Other Relations"

class has_borrowed_book(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    copy_no = models.IntegerField()
    checkout_date = models.DateTimeField(auto_now_add=True, blank=True)
    date_returned = models.DateTimeField(auto_now_add=True, blank=True)
    condition_before = models.CharField(max_length=500)
    condition_after = models.CharField(max_length=500)
    late_return_fee = models.IntegerField()

class has_borrowed_movie(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    copy_no = models.IntegerField()
    checkout_date = models.DateTimeField(auto_now_add=True, blank=True)
    date_returned = models.DateTimeField(auto_now_add=True, blank=True)
    condition_before = models.CharField(max_length=500)
    condition_after = models.CharField(max_length=500)
    late_return_fee = models.IntegerField()

class has_borrowed_other(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    otherItem = models.ForeignKey(OtherItem, on_delete=models.CASCADE)
    copy_no = models.IntegerField()
    checkout_date = models.DateTimeField(auto_now_add=True, blank=True)
    date_returned = models.DateTimeField(auto_now_add=True, blank=True)
    condition_before = models.CharField(max_length=500)
    condition_after = models.CharField(max_length=500)
    late_return_fee = models.IntegerField()

class book_is_of(models.Model):
    item = models.ForeignKey(Book, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, null=True, on_delete=models.SET_NULL)
    
    #def __str__(self):
	#   return self.genre

    class Meta:
      verbose_name_plural = "Book Genres"

class movie_is_of(models.Model):
    item = models.ForeignKey(Movie, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, null=True, on_delete=models.SET_NULL)
    
    #def __str__(self):
	 #   return self.genre

    class Meta:
      verbose_name_plural = "Movie Genres"

class other_is_of(models.Model):
    item = models.ForeignKey(OtherItem, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, null=True, on_delete=models.SET_NULL)

    #def __str__(self):
	#    return self.genre

    class Meta:
      verbose_name_plural = "Other Item Genres"

class Written_by(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    class Meta:
      verbose_name_plural = "Written by Relations"
