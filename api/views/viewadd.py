from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from ..models import *
from ..serializers import *
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.conf import settings
from django.core.exceptions import ValidationError
import traceback

class CreateBookView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data.copy()
        author = get_object_or_404(Author, name=request.data.get('author'))
        data['author'] = author.id
        
        serializer = BookSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CreateAuthorView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data.copy()

        serializer = AuthorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AddBookToFavoritesView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, book_pk):
        book = get_object_or_404(Book, pk=book_pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)

    def post(self, request, book_pk):
        try:
            book = get_object_or_404(Book, pk=book_pk)
            user = request.user

            # Check if the book is already in the user's favorites
            if FavoriteBook.objects.filter(user=user, book=book).exists():
                raise ValidationError("This book is already in your favorites.")

            # Add the book to the user's favorites
            favorite_book = FavoriteBook(user=user, book=book)
            favorite_book.save()

            # Retrieve the author of the book
            author = book.author

            suggested_books = Book.objects.filter(author=author).exclude(pk=book.pk)

            suggested_books_data = [
                {
                    "id": suggested_book.id,
                    "title": suggested_book.book_name,
                    "author": suggested_book.author.name,
                    "description": suggested_book.description
                }
                for suggested_book in suggested_books
            ]

            # Return the response including the success message and suggested books
            return Response({
                "message": "Book successfully added to favorites!",
                "suggested_books": suggested_books_data  # Return the list of suggested books
            }, status=status.HTTP_201_CREATED)

        except Exception as e:
            if settings.DEBUG:
                message = (
                    f"***** ---> str(e): {str(e)} "
                    f"***** ---> e.args: {str(e.args)} "
                    f"***** ---> type(e): {type(e).__name__} "
                    f"***** ---> traceback: {traceback.format_exc()}"
                )
            else:
                message = "An unexpected error occurred. Please contact support."
            return Response({"error": message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    def add_book_to_favorites(book, user):
        if FavoriteBook.objects.filter(user=user, book=book).exists():
            raise ValidationError("This book is already in your favorites.")

        favorite_book = FavoriteBook(user=user, book=book)
        favorite_book.save()
        return favorite_book        