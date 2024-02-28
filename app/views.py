from django.shortcuts import render
from .models import Smartphone
from django.http import HttpResponse, JsonResponse, HttpRequest
import json
# Create your views here.
def get_all(request: HttpRequest):
    data = Smartphone.objects.all()
    ruyxat = []
    for item in data:
        ruyxat.append(item.to_dict())
    return JsonResponse(ruyxat, safe=False)

def get_id(request: HttpRequest, id: int):
    
    try:
        data = Smartphone.objects.get(id=id)
        return JsonResponse(data.to_dict())
    except:
        HttpResponse("Smartphone not found id")

def get_add(request: HttpRequest):
    if request.method == "POST":
        data = request.body.decode('utf-8')
        data = json.loads(data)
        print(data)
        f = Smartphone.objects.create(
            name = data['name'],
            company = data['company'],
            color = data['color'],
            RAM = data['RAM'],
            memory = data['memory'],
            price = data['price'],
            img_url = data['img_url'],
        )
        return HttpResponse(f)
    else:
        HttpResponse("Method not found")

def get_id_update(request: HttpRequest, id: int):
    try:
        data = Smartphone.objects.filter(id=id).update(
            name = "Infinix Hot 11 Play",
            price = 133.0
        )
        data = Smartphone.objects.all()
        ruyxat = []
        for item in data:
            ruyxat.append(item.to_dict())
        return JsonResponse(ruyxat, safe=False)
    except:
        return HttpResponse("ID error")

def get_id_delete(request: HttpRequest, id: id):
    try:
        f = Smartphone.objects.filter(id=id).delete()
        data = Smartphone.objects.all()
        ruyxat = []
        for item in data:
            ruyxat.append(item.to_dict())
        return JsonResponse(ruyxat, safe=False)
    except:
        return HttpResponse("ID error")

