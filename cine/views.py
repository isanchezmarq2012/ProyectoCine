from django.http import HttpResponse


def index(request):
    return HttpResponse("Bienvenidos a The Lair Cinema =) ")

def cartelera(request):
    return HttpResponse("ESTA ES LA CARTELERA")

def tienda(request):
    return HttpResponse("Que deseas compar:")
