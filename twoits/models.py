import random

from django.db import models

# Create your models here.


class Twoit(models.Model):
    # id = models.autoField(primary_key=True)
    content = models.TextField(blank=True, null=True)
    image = models.FileField(upload_to='images/', blank=True, null=True)

    class Meta:
        # adding '-' with id indicates we'll be using descending ordering by id
        ordering = ['-id']

    # we'll use this method to format our twoit objects
    def serialize(self):
        return {
            "id": self.id,
            "content": self.content,
            "likes": random.randint(0, 10)
        }


