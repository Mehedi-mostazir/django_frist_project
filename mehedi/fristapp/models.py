from django.db import models
from django.utils import timezone


# Create your models here.
class appvaraity(models.Model):
  APP_TYPE_CHOICE = [
    ('ML', 'MACHINE LEARNING APP'),
    ('AI', 'ARTIFICIAL INTELIGENCE APP'),
    ('SC', 'SOCIAL MEDIA APP'),
    ('VI', 'VIDEO STREAMINMG APP'),
  ]
  name = models.CharField(max_length=100)
  image = models.ImageField(upload_to='apps/')
  date_added = models.DateTimeField(default=timezone.now)
  type = models.CharField(max_length=2, choices=APP_TYPE_CHOICE)
  description = models.TextField(default='')


  def __str__(self):
    return self.name
 
