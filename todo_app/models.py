from django.db import models
import datetime

# Create your models here.
class todoform(models.Model):
    tittle = models.CharField(max_length=50)
    note = models.TextField()
    #date = models.DateField(auto_now_add= True)
    date = models.DateField(("Date"), default=datetime.date.today)

    def __str__(self):
        return self.title