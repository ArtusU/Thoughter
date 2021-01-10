from django.db import models
from django.db.models.fields.files import ImageField

class Thought(models.Model):
    content                 = models.TextField(blank=True, null=True)
    ImageField              = models.FileField(upload_to='images/', blank=True, null=True)

   
