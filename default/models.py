from django.db import models

# Create your models here.
class Poll(models.Model):
    suject = models.CharField(max_length=255)
    description = models.TextField()
    date_created = models.DateField(auto_now_add=True)


    
class Option(models.Model):
    poil_id = models.IntegerField()
    title = models.CharField(max_length=200)
    count = models.IntegerField(default=0)



    