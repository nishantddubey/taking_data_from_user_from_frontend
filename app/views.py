from django.shortcuts import render
from app.models import *
# Create your views here.
from django.http import HttpResponse

def create_topic(request):
    if request.method=='POST':
        tn = request.POST.get('tn') 
        
        T=Topic.objects.get_or_create(topic_name=tn)[0]
        T.save()  
        return HttpResponse("Topic Inserted")   
    return render(request,'create_topic.html')

def create_webpage(request):
    if request.method=='POST':
        tn = request.POST.get('tn')
        name =request.POST.get('name')
        url = request.POST.get('url')
        
        T=Topic.objects.get_or_create(topic_name=tn)[0]
        T.save()
        
        W=Webpage.objects.get_or_create(topic_name=T,name=name,url=url)[0]
        W.save()
        return HttpResponse('webpage Inserted')
    return render(request,'create_webpage.html')