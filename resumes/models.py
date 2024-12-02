from django.db import models


class Resume(models.Model):
    title = models.CharField(max_length=100)
    skill = models.CharField(max_length=100)
    content = models.TextField(null=True)


# Create your models here.
