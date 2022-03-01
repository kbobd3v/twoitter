from django.db import models

# Create your models here.


class Twoit(models.Model):
    # id = models.autoField(primary_key=True)
    content = models.TextField(blank=True, null=True)
    image = models.FileField(upload_to='images/', blank=True, null=True)



