from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_on = models.DateTimeField()

    class Meta:
        ordering = ['-published_on']

    def __str__(self):
        return self.title
