from django.urls import path
from .views import BookDetail, BookListView, BookCreateView, index_view
urlpatterns = [
    path('index',index_view.as_view(), name = 'index'),
    path('',BookListView.as_view(), name = 'book_list'),
    path('book_form/',BookCreateView.as_view(), name = 'book_form'),
    path('book/<int:pk>/',BookDetail.as_view(), name = 'book_detail')

]

