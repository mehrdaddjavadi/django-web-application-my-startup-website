from django.urls import path
from articles import views
app_name="menus"
urlpatterns = [
    path("remote-sensing/Vegetation/",views.vegetation_cover,name="vegetation"),
    path("remote-sensing/precision-agriculture/",views.precision_agriculture,name="precision_agriculture"),
    path("computer-vision/object-detection/",views.object_detection,name="object_detection"),
    path("geomatics/surveying-geodesy/",views.mapping,name="mapping"),
    path("disaster-management/subsidence/",views.subsidence,name="subsidence"),
    path("disaster-management/flood/",views.flood,name="flood"),
    path("gis/toolbox/",views.toolbox,name="toolbox"),
    path("gis/siteselection/",views.siteselection,name="siteselection"),
    path("Work-with-us/",views.work,name="work"),
    path("about-us/",views.about,name="about"),
]
