from django.http import HttpResponse

# Create your views here.
def vista1(request):
    return HttpResponse("<h1>Vista 1</h1><p>Esto es una vista en app1</p><a href='#'>Enlace</a>")

def vista2(request):
    return HttpResponse("<h1>Vista 2</h1><p>Otra vista en app1</p><a href='#'>Otro enlace</a>")