from pyexpat import model
from django.urls import reverse
from django.db import models
from matplotlib.pyplot import cla

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class Author(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    date_of_birth = models.DateField(null=True,blank=True)

    class Meta:
        ordering = ['lname','fname']

    def get_absolute_url(self):
        return reverse("author_detail",kwargs={"pk":self.pk})
    
    def __str__(self):
        return f"{self.lname} {self.fname}"    

class Language(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author',on_delete=models.SET_NULL,null=True)
    summery = models.TextField(max_length=800)
    isbn = models.CharField('ISBN',max_length=12,unique=True) 
    genre = models.ManyToManyField(Genre)
    language = models.ForeignKey('Language',on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("book_detail", kwargs={"pk": self.pk})
    
import uuid

class BookInstance(models.Model):
    id =models.UUIDField(primary_key=True,default=uuid.uuid4)
    book = models.ForeignKey('Book',on_delete=models.RESTRICT,null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True,blank=True)

    Loan_Status = (
        ('m','Maintenance'),
        ('o','On Lone'),
        ('a','Available'),
        ('r','Reserved'),
    )
    status = models.CharField(max_length=1,choices=Loan_Status,blank=True,default='m')

    class Meta:
        ordering = ['due_back']

    def __str__(self):
        return f"{self.id} ({self.book.title})"