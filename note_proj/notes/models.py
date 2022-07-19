from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.


class Text(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=300)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title
