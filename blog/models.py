from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=10)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/') #So at max all the sizes of the boc=xes are same, as if some have more len then longer box and then unsemmetry
 
