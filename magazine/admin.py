from django.contrib import admin
from .models import EmailForMagazine



# Register your models here.




@admin.register(EmailForMagazine)

class EmailForMagazineAdmin(admin.ModelAdmin):


    list_display = ('email','joined')
    list_filter = ('email','joined')
    search_fields = ('email','joined')
    ordering = ('joined',)