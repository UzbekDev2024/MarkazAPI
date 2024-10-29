from django.urls import path

from .views import (
    # BookListAPI, BookDetailAPI,
    # BookUpdateAPI, BookCreateAPI,
    # BookDeleteAPI,
    # BookRetriveUpadateAPI, BookDeleteRetrieveAPI,

BookListCreateAPI, BookDetailUpdateDelete, BookListAPIView, BookCreateAPIView, BookDetailAPIView, BookUpdateAPIView, BookDeleteAPIVIew
)

urlpatterns = [
    path("list-create/", BookListCreateAPI.as_view()),

    path("list/", BookListAPIView.as_view()),
    path("create/", BookCreateAPIView.as_view()),
    path("detail/<int:pk>", BookDetailAPIView.as_view()),
    path("edit/<int:pk>", BookUpdateAPIView.as_view()),
    path("delete/<int:pk>", BookDeleteAPIVIew.as_view()),
    path("<int:pk>/delete-edit-detail", BookDetailUpdateDelete.as_view()),
    #
    # path("list/", BookListAPI.as_view()),
    # path("detail/<int:pk>/", BookDetailAPI.as_view()),
    # path("detail-update/<int:pk>/", BookRetriveUpadateAPI.as_view()),
    # path("delete-detail/<int:pk>/", BookDeleteRetrieveAPI.as_view()),
    # path("edit/<int:pk>/", BookUpdateAPI.as_view()),
    # path("create/", BookCreateAPI.as_view()),
    # path("delete/<int:pk>/", BookDeleteAPI.as_view()),
]
