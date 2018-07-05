from django.db import models
from django.utils import timezone

class Topic(models.Model):
    name = models.CharField(primary_key=True, max_length=45)
    description = models.CharField(max_length=255)
    created_date = models.DateTimeField(default=timezone.now, editable=False)
    updated_date = models.DateTimeField(blank=True, null=True)

class Post(models.Model):
    topic_name = models.ForeignKey('Topic')
    title = models.CharField(primary_key=True, max_length=100)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
