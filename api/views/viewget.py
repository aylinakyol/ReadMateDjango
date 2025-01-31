from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.conf import settings
import traceback
from ..serializers import *
from django.contrib.auth.models import User
from api.models import *
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

@api_view(['GET'])
def get_users(request):
    try:
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
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
@api_view(['GET'])
def get_authors(request):
    try:
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
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
@api_view(['GET'])
def get_books(request):
    try:
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
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
@api_view(['GET'])
def get_book_by_id(request, book_id):
    try:
        book = Book.objects.get(id=book_id)
        serializer = BookSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Book.DoesNotExist:
        return Response({"error": "Book not found."}, status=status.HTTP_404_NOT_FOUND)
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
@api_view(['GET'])
def get_author_by_id(request, author_id):
    try:
        author = Author.objects.get(id=author_id)
        serializer = AuthorSerializer(author)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Book.DoesNotExist:
        return Response({"error": "Book not found."}, status=status.HTTP_404_NOT_FOUND)
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

class GetFavoriteBooksView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        
        # Retrieve the list of books in the user's favorites
        favorite_books = FavoriteBook.objects.filter(user=user)

        # Serialize the books
        books_data = BookSerializer([favorite_book.book for favorite_book in favorite_books], many=True)

        return Response({
            "favorite_books": books_data.data
        }, status=status.HTTP_200_OK)                   