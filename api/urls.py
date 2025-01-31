from django.urls import path,include
from . import views
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [
    path('register-user/', views.register_user),
    path('login-user/', TokenObtainPairView.as_view(), name='token_obtain_pair'),

    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('get-users', views.get_users),
    path('get-authors', views.get_authors),
    path('get-books', views.get_books),

    path('get-book/<int:book_id>/', views.get_book_by_id),
    path('get-author/<int:author_id>/', views.get_author_by_id),
    path('get-favorite-books/', GetFavoriteBooksView.as_view(), name='favorite-books'),

    path('update-book/<int:book_pk>/', UpdateBookView.as_view(), name='update-book'),
    path('update-author/<int:author_pk>/', UpdateAuthorView.as_view(), name='update-author'),
    
    path('add-book/', CreateBookView.as_view(), name='add-book'),
    path('add-author/', CreateAuthorView.as_view(), name='add-author'),
    path('add-favorite-book/<int:book_pk>/', AddBookToFavoritesView.as_view(), name='add-favorites'),

    path('delete-book/<int:book_pk>/', RetrieveDestroyBookView.as_view(), name='delete-book'),
    path('delete-author/<int:author_pk>/', RetrieveDestroyAuthorView.as_view(), name='delete-author'),
    path('delete-favorite-book/<int:book_pk>/', RetrieveDestroyFavoriteView.as_view(), name='delete-favorites'),
]
