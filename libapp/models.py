from django.db import models

class Books(models.Model):
     user=models.CharField(max_length=100)
     email=models.CharField(max_length=100)
     title = models.CharField(max_length=100)
     author = models.CharField(max_length=100)
     published_date=models.DateField()
     borrowed_date = models.DateField()
     return_date = models.DateField(null=True, blank=True)

     def __str__(self):
       return self.title
     