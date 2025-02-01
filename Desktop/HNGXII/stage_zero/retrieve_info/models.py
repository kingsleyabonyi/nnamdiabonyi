from django.db import models

# Create your models here.
class UserInfo(models.Model):
    email = models.CharField(max_length=225)
    current_datetime = models.DateTimeField(auto_now_add=True)
    github_url = models.URLField()
