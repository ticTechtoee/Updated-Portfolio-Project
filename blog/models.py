from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length = 100)
    pub_date = models.CharField(max_length = 12)
    body = models.CharField(max_length = 400)
    image = models.ImageField(upload_to='images/')
    
    