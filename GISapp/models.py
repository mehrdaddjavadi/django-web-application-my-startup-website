from django.contrib.gis.db import models
# from __future__ import unicode_literals
from django.contrib.auth import get_user_model

class layers(models.Model):
    layer_id = models.AutoField(primary_key=True)
    layer_name = models.CharField(max_length=50)
    workspace = models.CharField(max_length = 50)
    layer_alias = models.CharField(max_length=50)
    server_address = models.URLField()
    userOwner = models.ManyToManyField(get_user_model())

    def __unicode__(self):
        return "   []     |   []:[]    |    []".format(self.layer_alias,self.workspace,self.layer_name,server_address)

class drawing(models.Model):
    geomId = models.AutoField(primary_key=True)
    geom = models.GeometryField()
    userOwner = models.ManyToManyField(get_user_model())

    def __str__(self):
        return str(self.geom)

