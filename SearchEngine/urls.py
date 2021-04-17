from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import *
from django.contrib import admin
admin.site.site_header="Log in as Admin User"
admin.site.site_title="welcome to koogle"
admin.site.index_title="Admin"
urlpatterns=[
path('',views.home,name="home"),
path('search',views.search,name="search"),
path('results',views.results,name="results"),
path('image/<int:id>/<slug:query>',views.image,name="image"),

]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)