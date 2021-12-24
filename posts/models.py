from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    # created_at = models.DateTimeField(auto_created=True)
    created_at = models.DateTimeField(auto_now_add=True)