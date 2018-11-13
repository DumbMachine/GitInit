from django.db import models

# Create your models here.
class Job(models.Model):
    #image for the Job
    image = models.ImageField(upload_to='images/')
    #description of the Job
    summary = models.CharField(max_length=200) #So at max all the sizes of the boc=xes are same, as if some have more len then longer box and then unsemmetry
