from django.http import JsonResponse
from time import sleep

def Slow_view(request):
    data = {
        "name": "Muhammed Ali"
    }
    sleep(5)
    return JsonResponse(data)