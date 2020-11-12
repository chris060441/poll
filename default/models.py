from django.db import models

# Create your models here.
class Poll(models.Model):
    suject = models.CharField(max_length=200)
    description = models.TextField()
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.id) + ") " + self.subject

class Option(models.Model):
    poil_id = models.IntegerField()
    title = models.CharField(max_length=200)
    count = models.IntegerField(default=0)
    
    def__str__(self):
        return str(self.id) + ")" + self.title + "@" + str(self.poll_id)