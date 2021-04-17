from django.db import models
from django.utils.html import format_html
class Image(models.Model):
    

    name=models.CharField(max_length=100)
    img=models.ImageField(upload_to='pics')
    def Images(self):
        return format_html('<img src="%s" style="width: 100px; height:100px;" />' % self.img.url)
    Images.allow_tags = True
   


# Create your models here.
