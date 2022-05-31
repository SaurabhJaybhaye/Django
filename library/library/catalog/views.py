from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView,ListView,CreateView,DetailView
from .models import Book

# Create your views here.
class index_view(TemplateView):
    template_name= 'catalog/index.html'

class BookListView(ListView):
    model= Book
    context_object_name="bookslist"

class BookCreateView(LoginRequiredMixin,CreateView):
    model = Book
    fields="__all__"

class BookDetail(DetailView):
    model= Book