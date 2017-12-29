import json

from django.http import JsonResponse, HttpResponseServerError, HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from map.mongo import locationJson, gasInfoApi, gasInfoApiByDay,sumGas


def googleMap(request):
    content = {"content":"this is javascript link"}
    return render(request,"googlemap.html",content)


def locationApi(request):
    queryset = locationJson()
    # content = {"json":queryset}
    return JsonResponse(queryset,safe=False)
@csrf_exempt
def gasInfo(request):
    if request.method != 'POST':
        # not POST?
        return HttpResponseServerError("Only POST method allowed!")
    elif request.POST:
        stn = request.POST["station"]

        queryset =gasInfoApi(stn)
        return JsonResponse(queryset,safe=False)

def gasApiV2(request,stn,date):
    if stn and date:
        queryset = gasInfoApiByDay(stn,date)
        return JsonResponse(queryset,safe=False)

@csrf_exempt
def sumOfGas(request):
    if request.method != 'POST':
        # not POST?
        return HttpResponseServerError("Only POST method allowed!")
    elif request.POST:
        stn = request.POST["station"]
        startDate = request.POST["startDate"]
        endDate = request.POST["endDate"]
        queryset = sumGas(startDate,endDate,stn)
        #print(queryset)
        return JsonResponse(queryset,safe=False)


