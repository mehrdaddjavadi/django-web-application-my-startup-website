from django.db import models


class Contact(models.Model):
    first_name = models.CharField(max_length=250,)
    last_name = models.CharField(max_length=250,)
    email = models.EmailField(max_length=254,blank=True, null=True)
    subject = models.TextField()

    def __str__(self):
        return self.first_name + " " + self.last_name
    

