from django.contrib import admin

from GISapp.models import layers, drawing

# @admin.register(layers)
# class LayerAdmin(admin.ModelAdmin):
#     # list_display = ('layer_id','layer_name','workspace','layer_alias',' server_address',' userOwner')
#     # list_filter = ( 'userOwner','layer_alias','server_address','layer_name')
#     # search_fields = ('userOwner','layer_alias','server_address','layer_name')
#     pass


# @admin.register(drawing)
# class DrawingAdmin(admin.ModelAdmin):
#     # list_display = ('layer_id','layer_name','workspace','layer_alias',' server_address',' userOwner')
#     # list_filter = ( 'userOwner','layer_alias','server_address','layer_name')
#     # search_fields = ('userOwner','layer_alias','server_address','layer_name')
#     pass
admin.site.register(drawing)
admin.site.register(layers)