from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('author/', views.AuthorsList, name='authors'),
    path('author/<int:pk>/', views.AuthorDetail, name='author-detail'),

    path('publisher/', views.PublishersList, name='publishers'),
    path('publisher/<int:pk>/', views.PublisherDetail, name='publishers-detail'),

    path('otherItem/', views.OtherItems, name='otherItem'),
    path('otherItem/<int:pk>/', views.OtherItemDetail, name='otherItem-detail'),

    path('movie/', views.Movies, name='movie'),
    path('movie/<int:pk>/', views.MovieDetail, name='movie-detail'),

    path('book/', views.Books, name='book'),
    path('book/<int:pk>/', views.BookDetail, name='book-detail'),

    path('staff/', views.Staffs, name='staff'),
    path('staff/<int:pk>/', views.StaffDetail, name='staff-detail'),

    path('manager/', views.Managers, name='manager'),
    path('manager/<int:pk>/', views.ManagerDetail, name='manager-detail'),

    path('branch/', views.Branches, name='branch'),
    path('branch/<int:pk>/', views.BranchDetail, name='branch-detail'),

    path('collection/', views.Collections, name='collection'),
    path('collection/<int:pk>/', views.CollectionDetail, name='collection-detail'),

    path('genre/', views.Genres, name='genre'),
    path('genres/<int:pk>/', views.GenreDetail, name='genre-detail'),

    path('copyBook/', views.CopiesBook, name='copyBook'),
    path('copyBook/<int:pk>/', views.CopyBookDetail, name='copyBook-detail'),

    path('copyOtherItem/', views.CopiesOtherItem, name='copyOtherItem'),
    path('copyOtherItem/<int:pk>/', views.CopyOtherItemDetail, name='copyOtherItem-detail'),

    path('copyMovie/', views.CopiesMovie, name='copyMovie'),
    path('copyMovie/<int:pk>/', views.CopyMovieDetail, name='copyMovie-detail'),

    path('isBorrowingBook/', views.IsBorrowingBooks, name='isBorrowingBook'),
    path('isBorrowingBook/<int:pk>/', views.IsBorrowingBookDetail, name='isBorrowingBook-detail'),

    path('isBorrowingMovie/', views.IsBorrowingMovies, name='isBorrowingMovie'),
    path('isBorrowingMovie/<int:pk>/', views.IsBorrowingMovieDetail, name='isBorrowingMovie-detail'),

    path('isBorrowingOther/', views.IsBorrowingOthers, name='isBorrowingOther'),
    path('isBorrowingOther/<int:pk>/', views.IsBorrowingOtherDetail, name='isBorrowingOther-detail'),

    path('bookIsOf/', views.BookIsOfs, name='bookIsOf'),
    path('bookIsOf/<int:pk>/', views.BookIsOfDetail, name='bookIsOf-detail'),

    path('movieIsOf/', views.MovieIsOfs, name='movieIsOf'),
    path('movieIsOf/<int:pk>/', views.MovieIsOfDetail, name='movieIsOf-detail'),

    path('otherIsOf/', views.OtherIsOfs, name='otherIsOf'),
    path('otherIsOf/<int:pk>/', views.OtherIsOfDetail, name='otherIsOf-detail'),

    path('writtenBy/', views.WrittenBys, name='writtenBy'),
    path('writtenBy/<int:pk>/', views.WrittenByDetail, name='writtenBy-detail'),
]