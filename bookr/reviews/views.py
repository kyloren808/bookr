from django.http import HttpResponse

def index(request):
    name = request.GET.get("name") or "World"
    return HttpResponse(f"Hello, {name}. You're at the reviews index.")
