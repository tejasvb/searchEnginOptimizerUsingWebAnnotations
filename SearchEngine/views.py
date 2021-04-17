from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Image

# Create your views here.
def search(request):
    images=Image.objects.all()

    
    return render(request,'search.html',{'images':images})

def results(request):
    
    query=request.GET['query']

    images=Image.objects.filter(name__icontains =query)    
    
    
    params={'images': images, 'query': query}
    return render(request, 'results.html', params)
  
def image(request,id,query):
    images=Image.objects.filter(name__icontains =query)  
    selectedImage=Image.objects.filter(id__icontains =id)   
    params={'images': images,'selectedImage': selectedImage,'query':query,'SelectedImageid':id}
    return render(request,'image.html', params)

def home(request):
     return render(request,'home.html')

  
# Create your views here.
  
  
  

