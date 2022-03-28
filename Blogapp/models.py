from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class ContactDetails(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.TextField()
    phoneno = models.CharField(max_length=10)
    state = models.CharField(max_length=20)
    city = models.CharField(max_length=20)

    def __str__(self):
        return self.name