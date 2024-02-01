from django.db import models

class Room(models.Model):
    name= models.CharField(max_length=200)
    description=models.TextField(null=True,blank=False)
    image=models.ImageField(upload_to='images')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.name
    
