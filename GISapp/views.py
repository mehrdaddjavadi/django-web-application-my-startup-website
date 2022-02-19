from django.shortcuts import render
from .models import layers, drawing
from django.core import serializers
from django.http import HttpResponse

def myfarm_view(request):
    return render(request,'GISapp/myfarm.html')

def getwms(request):
    if request.user.is_authenticated():
        layersG = layers.objects.filter(userOwner = request.user)
        layersGJSON = serializers.serialize('json', layersG)
    else:
        layersGJSON=""
    return HttpResponse(layersGJSON, content_type='text/html')


def get_drawings(request):
    if request.user.is_authenticated:
        drawingObjs = drawing.objects.filter(userOwner = request.user)

        drawingObjsJSON = serializers.serialize('geojson', drawingObjs)
        return HttpResponse(drawingObjsJSON, content_type='text/html')

    else:
        return HttpResponse('Access Denied. Error 403', content_type='text/html')
        
