from django.db import models

from apps.social.models import User


# Create your models here.
class Review(models.Model):
    book_id = models.CharField(max_length=12)
    comment = models.TextField()
    rate = models.FloatField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
