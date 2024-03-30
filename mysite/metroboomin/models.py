from django.db import models

# Create your models here.

class train (models.Model) :
    
    id = models.AutoField(primary_key = True)
    datetime = models.CharField(max_length = 20)
    destination = models.CharField(max_length = 200)
    plan = models.CharField(max_length = 2000)    

