from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from ..models import Author, Book, FavoriteBook
from ..serializers import BookSerializer, AuthorSerializer  # Add AuthorSerializer if you don't have one

class RetrieveDestroyBookView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, book_pk):
        book = get_object_or_404(Book, pk=book_pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)

    def delete(self, request, book_pk):
        book = get_object_or_404(Book, pk=book_pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class RetrieveDestroyAuthorView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, author_pk):
        author = get_object_or_404(Author, pk=author_pk)
        serializer = AuthorSerializer(author)
        return Response(serializer.data)

    def delete(self, request, author_pk):
        author = get_object_or_404(Author, pk=author_pk)
        author.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class RetrieveDestroyFavoriteView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, book_pk):
        book = get_object_or_404(Book, pk=book_pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)

    def delete(self, request, book_pk):
        user = request.user
        book = get_object_or_404(Book, pk=book_pk)
        favorite_book = FavoriteBook.objects.filter(user=user, book=book)
        favorite_book.delete()
        return Response({
                "message": f"Book successfully deleted from favorites!"
            },status=status.HTTP_204_NO_CONTENT)