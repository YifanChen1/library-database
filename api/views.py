from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from media.models import Author, Publisher, OtherItem, Movie, Book, Staff, Manager, Branch, Collection, Genre, Copy_of_book, Copy_of_Other, Copy_of_Movies, is_borrowing_book, is_borrowing_movie, is_borrowing_other, book_is_of, movie_is_of, other_is_of, Written_by
from .serializers import AuthorSerializer, PublisherSerializer, OtherItemSerializer, MovieSerializer, BookSerializer, StaffSerializer, ManagerSerializer, BranchSerializer, CollectionSerializer, GenreSerializer, CopyBookSerializer, CopyOtherItemSerializer, CopyMovieSerializer, BorrowingBookSerializer, BorrowingMovieSerializer, BorrowingOtherSerializer, BookIsOfSerializer, MovieIsOfSerializer, OtherIsOfSerializer, WrittenBySerializer

#AUTHORS
@api_view(['GET', 'POST'])
def AuthorsList(request):
    if request.method == 'GET':
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE', 'POST'])
def AuthorDetail(request, pk):
    try:
        author = Author.objects.get(id=pk)
    except Author.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AuthorSerializer(author, many=False)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = AuthorSerializer(author, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        author.delete()
        return Response("Author deleted.")

#PUBLISHERS
@api_view(['GET', 'POST'])
def PublishersList(request):
    if request.method == 'GET':
        publishers = Publisher.objects.all()
        serializer = PublisherSerializer(publishers, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = PublisherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE', 'POST'])
def PublisherDetail(request, pk):
    try:
        publisher = Publisher.objects.get(id=pk)
    except Publisher.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PublisherSerializer(publisher, many=False)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = PublisherSerializer(publisher, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        publisher.delete()
        return Response("Publisher deleted.")

#OTHER ITEM
@api_view(['GET', 'POST'])
def OtherItems(request):
    if request.method == 'GET':
        things = OtherItem.objects.all()
        serializer = OtherItemSerializer(things, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = OtherItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE', 'POST'])
def OtherItemDetail(request, pk):
    try:
        thing = OtherItem.objects.get(id=pk)
    except OtherItem.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = OtherItemSerializer(thing, many=False)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = OtherItemSerializer(thing, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        thing.delete()
        return Response("Media item of type OtherItem deleted.")

#MOVIE
@api_view(['GET', 'POST'])
def Movies(request):
    if request.method == 'GET':
        things = Movie.objects.all()
        serializer = MovieSerializer(things, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE', 'POST'])
def MovieDetail(request, pk):
    try:
        thing = Movie.objects.get(id=pk)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MovieSerializer(thing, many=False)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = MovieSerializer(thing, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        thing.delete()
        return Response("Media item of type Movie deleted.")

#BOOK
@api_view(['GET', 'POST'])
def Books(request):
    if request.method == 'GET':
        things = Book.objects.all()
        serializer = BookSerializer(things, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE', 'POST'])
def BookDetail(request, pk):
    try:
        thing = Book.objects.get(id=pk)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BookSerializer(thing, many=False)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = BookSerializer(thing, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        thing.delete()
        return Response("Media item of type Book deleted.")

#STAFF
@api_view(['GET', 'POST'])
def Staffs(request):
    if request.method == 'GET':
        things = Staff.objects.all()
        serializer = StaffSerializer(things, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = StaffSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE', 'POST'])
def StaffDetail(request, pk):
    try:
        thing = Staff.objects.get(id=pk)
    except Staff.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StaffSerializer(thing, many=False)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = StaffSerializer(thing, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        thing.delete()
        return Response("Staff deleted.")

#MANAGER
@api_view(['GET', 'POST'])
def Managers(request):
    if request.method == 'GET':
        things = Manager.objects.all()
        serializer = ManagerSerializer(things, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = ManagerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE', 'POST'])
def ManagerDetail(request, pk):
    try:
        thing = Manager.objects.get(id=pk)
    except Manager.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ManagerSerializer(thing, many=False)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = ManagerSerializer(thing, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        thing.delete()
        return Response("Manager deleted.")

#BRANCH
@api_view(['GET', 'POST'])
def Branches(request):
    if request.method == 'GET':
        things = Branch.objects.all()
        serializer = BranchSerializer(things, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = BranchSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE', 'POST'])
def BranchDetail(request, pk):
    try:
        thing = Branch.objects.get(id=pk)
    except Branch.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BranchSerializer(thing, many=False)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = BranchSerializer(thing, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        thing.delete()
        return Response("Branch deleted.")

#COLLECTION
@api_view(['GET', 'POST'])
def Collections(request):
    if request.method == 'GET':
        things = Collection.objects.all()
        serializer = CollectionSerializer(things, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = CollectionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE', 'POST'])
def CollectionDetail(request, pk):
    try:
        thing = Collection.objects.get(id=pk)
    except Collection.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CollectionSerializer(thing, many=False)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = CollectionSerializer(thing, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        thing.delete()
        return Response("Collection deleted.")

#GENRE
@api_view(['GET', 'POST'])
def Genres(request):
    if request.method == 'GET':
        things = Genre.objects.all()
        serializer = GenreSerializer(things, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = GenreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE', 'POST'])
def GenreDetail(request, pk):
    try:
        thing = Genre.objects.get(id=pk)
    except Genre.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = GenreSerializer(thing, many=False)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = GenreSerializer(thing, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        thing.delete()
        return Response("Genre deleted.")

#COPY OF BOOK
@api_view(['GET', 'POST'])
def CopiesBook(request):
    if request.method == 'GET':
        things = Copy_of_book.objects.all()
        serializer = CopyBookSerializer(things, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = CopyBookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE', 'POST'])
def CopyBookDetail(request, pk):
    try:
        thing = Copy_of_book.objects.get(id=pk)
    except Copy_of_book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CopyBookSerializer(thing, many=False)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = CopyBookSerializer(thing, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        thing.delete()
        return Response("Copy of book deleted.")

#COPY OF OTHERITEM
@api_view(['GET', 'POST'])
def CopiesOtherItem(request):
    if request.method == 'GET':
        things = Copy_of_Other.objects.all()
        serializer = CopyOtherItemSerializer(things, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = CopyOtherItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE', 'POST'])
def CopyOtherItemDetail(request, pk):
    try:
        thing = Copy_of_Other.objects.get(id=pk)
    except Copy_of_Other.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CopyOtherItemSerializer(thing, many=False)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = CopyOtherItemSerializer(thing, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        thing.delete()
        return Response("Copy of OtherItem deleted.")

#COPY OF MOVIE
@api_view(['GET', 'POST'])
def CopiesMovie(request):
    if request.method == 'GET':
        things = Copy_of_Movies.objects.all()
        serializer = CopyMovieSerializer(things, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = CopyMovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE', 'POST'])
def CopyMovieDetail(request, pk):
    try:
        thing = Copy_of_Movies.objects.get(id=pk)
    except Copy_of_Movies.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CopyMovieSerializer(thing, many=False)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = CopyMovieSerializer(thing, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        thing.delete()
        return Response("Copy of Movie deleted.")

#IS BORROWING BOOK
@api_view(['GET', 'POST'])
def IsBorrowingBooks(request):
    if request.method == 'GET':
        things = is_borrowing_book.objects.all()
        serializer = BorrowingBookSerializer(things, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = BorrowingBookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE', 'POST'])
def IsBorrowingBookDetail(request, pk):
    try:
        thing = is_borrowing_book.objects.get(id=pk)
    except is_borrowing_book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BorrowingBookSerializer(thing, many=False)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = BorrowingBookSerializer(thing, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        thing.delete()
        return Response("Tuple of is_borrowing_book deleted.")

#IS BORROWING MOVIE
@api_view(['GET', 'POST'])
def IsBorrowingMovies(request):
    if request.method == 'GET':
        things = is_borrowing_movie.objects.all()
        serializer = BorrowingMovieSerializer(things, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = BorrowingMovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE', 'POST'])
def IsBorrowingMovieDetail(request, pk):
    try:
        thing = is_borrowing_movie.objects.get(id=pk)
    except is_borrowing_movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BorrowingMovieSerializer(thing, many=False)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = BorrowingMovieSerializer(thing, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        thing.delete()
        return Response("Tuple of is_borrowing_movie deleted.")

#IS BORROWING OTHERITEM
@api_view(['GET', 'POST'])
def IsBorrowingOthers(request):
    if request.method == 'GET':
        things = is_borrowing_other.objects.all()
        serializer = BorrowingOtherSerializer(things, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = BorrowingOtherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE', 'POST'])
def IsBorrowingOtherDetail(request, pk):
    try:
        thing = is_borrowing_other.objects.get(id=pk)
    except is_borrowing_other.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BorrowingOtherSerializer(thing, many=False)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = BorrowingOtherSerializer(thing, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        thing.delete()
        return Response("Tuple of is_borrowing_other deleted.")

#BOOK IS OF
@api_view(['GET', 'POST'])
def BookIsOfs(request):
    if request.method == 'GET':
        things = book_is_of.objects.all()
        serializer = BookIsOfSerializer(things, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = BookIsOfSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE', 'POST'])
def BookIsOfDetail(request, pk):
    try:
        thing = book_is_of.objects.get(id=pk)
    except book_is_of.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BookIsOfSerializer(thing, many=False)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = BookIsOfSerializer(thing, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        thing.delete()
        return Response("Tuple of book_is_of deleted.")

#MOVIE IS OF
@api_view(['GET', 'POST'])
def MovieIsOfs(request):
    if request.method == 'GET':
        things = movie_is_of.objects.all()
        serializer = MovieIsOfSerializer(things, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = MovieIsOfSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE', 'POST'])
def MovieIsOfDetail(request, pk):
    try:
        thing = movie_is_of.objects.get(id=pk)
    except movie_is_of.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MovieIsOfSerializer(thing, many=False)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = MovieIsOfSerializer(thing, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        thing.delete()
        return Response("Tuple of movie_is_of deleted.")

#OTHERITEM IS OF
@api_view(['GET', 'POST'])
def OtherIsOfs(request):
    if request.method == 'GET':
        things = other_is_of.objects.all()
        serializer = OtherIsOfSerializer(things, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = OtherIsOfSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE', 'POST'])
def OtherIsOfDetail(request, pk):
    try:
        thing = other_is_of.objects.get(id=pk)
    except other_is_of.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = OtherIsOfSerializer(thing, many=False)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = OtherIsOfSerializer(thing, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        thing.delete()
        return Response("Tuple of other_is_of deleted.")

#WRITTEN BY
@api_view(['GET', 'POST'])
def WrittenBys(request):
    if request.method == 'GET':
        things = Written_by.objects.all()
        serializer = WrittenBySerializer(things, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = WrittenBySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE', 'POST'])
def WrittenByDetail(request, pk):
    try:
        thing = Written_by.objects.get(id=pk)
    except Written_by.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = WrittenBySerializer(thing, many=False)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = WrittenBySerializer(thing, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        thing.delete()
        return Response("Tuple of Written_by deleted.")