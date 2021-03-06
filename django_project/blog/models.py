from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.
# Object relational Mapping


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)  # Delete a user to delete all the posts

    def __str__(self):
        return self.title

    # Once a post is created, a redirect is performed to the following url
    def get_absolute_url(self):
        # reverse method returns the url as a string
        return reverse('post-detail', kwargs={'pk': self.pk})
