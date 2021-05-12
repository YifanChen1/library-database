from django.shortcuts import render, redirect
from .models import Book
from .models import Movie
from .models import OtherItem
from .models import is_borrowing_book
from .models import is_borrowing_movie
from .models import is_borrowing_other
from django.contrib.auth.models import User
from datetime import datetime
#from .forms import EntryForm


def Userhome(request):

    return render(request, 'media/Index.html')

def Books(request):

    books = Book.objects.all()
    context = {'books' : books}
    return render(request, 'media/books.html', context)

def Movies(request):

    movies = Movie.objects.all()
    context = {'movies' : movies}
    return render(request, 'media/Movies.html', context)

def Otheritems(request):

    otheritems = OtherItem.objects.all()
    context = {'otheritems' : otheritems}
    return render(request, 'media/Otheritems.html', context)

def view(request):
    temp = User.objects.get(id = request.user.id)
    bor = is_borrowing_book.objects.filter(user = temp)
    book_list=[]
    for b in bor:
        book_list.append(b.book)
    bor2 = is_borrowing_movie.objects.filter(user = temp)
    for b in bor2:
        book_list.append(b.movie)
    bor3 = is_borrowing_other.objects.filter(user = temp)
    for b in bor3:
        book_list.append(b.otherItem)

    return render(request, 'media/view.html', locals())

def borrow(request, pk):
    all = OtherItem.objects.get(id = pk) + Book.objects.get(id = pk) + Movie.objects.get(id = pk)
    u = get_object_or_404(user,id = request.user.id)
    message = "book has been borrowed."
    a = is_borrowing_book()
    a.book = all
    a.user = u
    a.checkout_date = datetime.datetime.now()
    a.due_date = datetime.datetime.now() + datetime.timedelta(7)
    a.save()
    return redirect('media/Index.html')

def returnbook(request, pk):
    all = OtherItem.objects.get(id = pk) + Book.objects.get(id = pk) + Movie.objects.get(id = pk)
    u = get_object_or_404(user,id = request.user.id)
    a = has_borrowed_book()
    is_borrowing_book.get(id = u).delete()
    a.book = all
    a.user = u
    a.save
    return redirect('media/Index.html', locals())
