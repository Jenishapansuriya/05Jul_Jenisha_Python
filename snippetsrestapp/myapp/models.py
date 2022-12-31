from django.db import models

# Create your models here.

class snippets(models.Model):
    title=models.CharField(max_length=20)
    code=models.CharField(max_length=20)
    linenos=models.CharField(max_length=20)
    language=models.CharField(max_length=20)
    style=models.CharField(max_length=20)

    def __str__(self):
        return self.title