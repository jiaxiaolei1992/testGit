from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http.response import HttpResponse
from king1.models import Asset

# Create your views here.

def index(request):
    return HttpResponse('index')
def login(request,id):
    print id
    return HttpResponse('login')

def list(request,name,id):
    print name,id
    return HttpResponse('list')

def Add(request,name):
    Asset.objects.create(hostname=name)
    return HttpResponse('OK')

def delete(request,id):
    Asset.objects.get(id=id).delete()
    return HttpResponse('OK')

#1
def update(request,id,hostname):
    #1
    '''
    obj=Asset.objects.get(id=id)
    obj.hostname=hostname
    obj.save()
    return HttpResponse('OK')
    '''
    #2

    Asset.objects.filter(id__gt=id).update(hostname=hostname)
    return HttpResponse('OK')

def Get(request,hostname):
    #1
    '''
    assetList=Asset.objects.filter(hostname__contains=hostname)
    for item in assetList:
        print item.hostname

    return HttpResponse('OK')
    #2
    alldata=Asset.objects.all()
    temp=Asset.objects.all()[0:2]

    #3
    alldata=Asset.objects.all().order_by('-id')
    alldata=Asset.objects.all().order_by('id')

    #4
    temp=Asset.objects.all()[0:2]
    print temp.query

    #5
    temp1=Asset.objects.all().values('id','hostname')
    print temp1
    '''
    return HttpResponse('OK')

def AssetList(request):
    asset_list=Asset.objects.all()
    print asset_list

    result=render_to_response('showlist.html',{'data':asset_list,'user':'jiaxiaolei'})
    return result
















