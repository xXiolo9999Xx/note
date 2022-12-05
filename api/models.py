from django.db import models

# Create your models here.
class note(models.Model):
    body = models.TextField(null=False,blank=False)
    updated = models.DateTimeField(auto_now_add=True)
    created = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.body[0:50]