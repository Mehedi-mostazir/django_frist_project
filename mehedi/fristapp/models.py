from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

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
  

#One two many
class appreview(models.Model):
  app = models.ForeignKey(appvaraity, on_delete= models.CASCADE, related_name='reviews')
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  rating = models.IntegerField()
  comment = models.TextField()
  date_added = models.DateTimeField(default=timezone.now)

  def __str__(self):
      return f'{self.user.username} review for {self.app.name}'
  

# Many to many
class Store(models.Model):
   name = models.CharField(max_length=100)
   location = models.CharField(max_length=100)
   app_varieties = models.ManyToManyField(appvaraity, related_name= 'stores')
   

   def __str__(self):
       return self.name

# One to one

class appCertificate(models.Model):
   app = models.OneToOneField(appvaraity, on_delete=models.CASCADE, related_name= 'certificate')
   certificate_number = models.CharField(max_length=100)
   issued_date = models.DateTimeField(default=timezone.now)
   valid_untill = models.DateTimeField

   def __str__(self):
       return f'Certificate for {self.name.app}'
   

   

   