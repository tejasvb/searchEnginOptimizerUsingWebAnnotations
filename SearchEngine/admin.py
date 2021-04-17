from django.contrib import admin

from .models import Image
class ImageAdmin(admin.ModelAdmin):
    list_display=('name','img')
    search_fields=('name','img')
    list_editable=('name',)
    list_per_page=7
    list_display_links=('img',)
    list_display = ('img','name' , 'Images')
    
# Register your models here.
admin.site.register(Image,ImageAdmin)
# Register your models here.
