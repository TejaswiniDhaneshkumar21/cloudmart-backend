from django.http import JsonResponse

def home(request):
    return JsonResponse({
        "message": "Welcome to CloudMart ✅",
        "try": ["/health/", "/admin/"]
    })

def health(request):
    return JsonResponse({
        "status": "ok",
        "app": "cloudmart",
        "message": "CloudMart backend is running"
    })

