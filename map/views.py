from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from map.mongo import locationJson , gasInfoApi


def googleMap(request):
    content = {"content":"this is javascript link"}
    return render(request,"googlemap.html",content)


def locationApi(request):
    queryset = locationJson()
    # content = {"json":queryset}
    return JsonResponse(queryset,safe=False)

def gasInfo(request,id):
    print(id)
    quesyset = gasInfoApi(id)
    return JsonResponse(quesyset,safe=False)