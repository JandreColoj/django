from django.http import HttpResponse
import datetime

def index(request): #vista -> controlador
  
  return HttpResponse("Pagina principal de mi aplicacion Django")

def info(request): #vista -> controlador
  
  return HttpResponse("<h1 style='font-size:50px; color:#FF5733'>Informacion de pagina </h1>")


def fecha(request):

  fecha = datetime.datetime.now()
 
  return HttpResponse("<h1 style='font-size:50px; color:#FF5733'>la fecha de actual es %s </h1>" % fecha)

def edad(request, anio):
  
  edad = 2019-anio

  return HttpResponse("El anio  %s mi edad es %s" %(anio,edad))