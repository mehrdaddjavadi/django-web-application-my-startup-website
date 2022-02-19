from django.db import models

class EmailForMagazine(models.Model):
   email = models.EmailField(max_length=254, blank=True, null=True, unique=True);
   joined = models.TimeField(auto_now_add=True);

   def __str__(self):
       return self.email
   
