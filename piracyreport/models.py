from django.db import models

# Create your models here.

BOOK_STATUS = (
    ("Resolved","Resolved"),
    ("Unresolved","Unresolved"),
)

class TopList(models.Model):
    ISBN = models.CharField(max_length = 20, blank = False)
    Book_name = models.CharField(max_length = 150)

class Books(models.Model):
    ISBN = models.CharField(max_length = 20, blank = False)
    Book_name = models.CharField(max_length = 150)
    link = models.CharField(max_length=150)
    Status = models.CharField(max_length=20, choices = BOOK_STATUS, default = "Unresolved")
    No_of_file_hosters = models.IntegerField()

class RawData(models.Model):
    ISBN = models.CharField(max_length = 20, blank = False)
    link = models.CharField(max_length=150)
    date_found = models.DateField(null=True, blank=True)
    date_resolved = models.DateField(null=True, blank=True)
