from rest_framework.decorators import api_view,authentication_classes, permission_classes
from rest_framework.response import Response
from ..serializers import UserSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from ..models import *
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from django.contrib.auth.models import User
from rest_framework import authentication
from rest_framework import exceptions
from django.conf import settings
from django.core.exceptions import ValidationError
import traceback

@api_view(['POST'])
def register_user(request):
    try:
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user = User.objects.get(username=request.data['username'])
            user.set_password(request.data['password'])
            user.save()
            token = Token.objects.create(user=user)
            return Response({"user":serializer.data})
        return Response(serializer.errors)
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