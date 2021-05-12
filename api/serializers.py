from rest_framework import serializers
from media.models import Author, Publisher, OtherItem, Movie, Book, Staff, Manager, Branch, Collection, Genre, Copy_of_book, Copy_of_Other, Copy_of_Movies, is_borrowing_book, is_borrowing_movie, is_borrowing_other, book_is_of, movie_is_of, other_is_of, Written_by

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = '__all__'

class OtherItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OtherItem
        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = '__all__'

class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = '__all__'

class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = '__all__'

class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = '__all__'

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class CopyBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Copy_of_book
        fields = '__all__'

class CopyOtherItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Copy_of_Other
        fields = '__all__'

class CopyMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Copy_of_Movies
        fields = '__all__'

class BorrowingBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = is_borrowing_book
        fields = '__all__'

class BorrowingMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = is_borrowing_movie
        fields = '__all__'

class BorrowingOtherSerializer(serializers.ModelSerializer):
    class Meta:
        model = is_borrowing_other
        fields = '__all__'

class BookIsOfSerializer(serializers.ModelSerializer):
    class Meta:
        model = book_is_of
        fields = '__all__'

class MovieIsOfSerializer(serializers.ModelSerializer):
    class Meta:
        model = movie_is_of
        fields = '__all__'

class OtherIsOfSerializer(serializers.ModelSerializer):
    class Meta:
        model = other_is_of
        fields = '__all__'

class WrittenBySerializer(serializers.ModelSerializer):
    class Meta:
        model = Written_by
        fields = '__all__'
