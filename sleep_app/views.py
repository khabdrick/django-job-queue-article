from django.http import JsonResponse
from django_q.tasks import async_task


def Slow_view(request):
    data = {
        "name": "Muhammed Ali"
    }
    async_task("sleep_app.q_services.py.sleepy_func", 7, hook="sleep_app.q_services.py.hook_funcs")
    return JsonResponse(data)