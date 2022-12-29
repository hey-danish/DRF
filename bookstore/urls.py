from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from bookstore import views

urlpatterns = format_suffix_patterns([
    path('', views.bookstore_root, name='bookstore_root'),
    path('books/', views.BooksList.as_view(), name='books-list'),
    path('books/<int:pk>/', views.BooksDetail.as_view(), name='books-detail'),
    path('authors/', views.AuthorsList.as_view(), name='authors-list'),
    path('authors/<int:pk>/', views.AuthorsDetail.as_view(), name='authors-detail'),
    path('publications/',views.PublishersList.as_view(), name='publications-list'),
    path('publications/<int:pk>/',views.PublishersDetail.as_view(), name='publications-detail'),

])
