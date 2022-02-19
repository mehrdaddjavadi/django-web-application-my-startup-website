from . import views
from django.urls import path
app_name='contactus'
urlpatterns = [
    path('',views.contactus_view,name="contactus")
]
