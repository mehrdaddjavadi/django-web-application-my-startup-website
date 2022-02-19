from .views import myfarm_view,getwms,get_drawings
from django.urls import path
app_name="GISapp"
urlpatterns = [
    path("myfarm/",myfarm_view,name='myfarm'),
    path('getwms/',getwms),
    # path('getdrawings/',get_drawings,name ='getdrawings')
]
