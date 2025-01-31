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

class UpdateBookView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, book_pk):
        book = get_object_or_404(Book, id=book_pk)
        
        serializer = BookSerializer(book, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UpdateAuthorView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, author_pk):
        author = get_object_or_404(Author, id=author_pk)
        
        serializer = AuthorSerializer(author, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)        