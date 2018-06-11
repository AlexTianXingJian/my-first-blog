from django.db import models
from django.utils import timezone


class Post(models.Model):
    auth = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_time = models.DateTimeField(default=timezone.now())
    published_time = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_time = timezone.now()
        self.save()

    def __str__(self):
        return self.title

