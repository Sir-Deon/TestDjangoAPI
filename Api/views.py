from django.http import response
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CitySerializer
from .models import City


# Create your views here.

@api_view(['GET'])
def test(request):
    api_urls = {
        'List': '/list_cities/',
        'AddCity': '/add_city/',
        'UpdateCity': '/update_city/id',
        'DeleteCity': '/delete_city/id'
    }
    return Response(api_urls)

@api_view(['GET'])
def listCity(request):
    cities = City.objects.all()
    serializer = CitySerializer(cities, many=True)
    return Response(serializer.data)



@api_view(['POST']) 
def addCity(request):
    serializer = CitySerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)




@api_view(['PUT']) 
def updateCity(request, pk):
    city  = City.objects.get(id=pk)
    serializer = CitySerializer(instance=city, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE']) 
def deleteCity(request, pk):
    city  = City.objects.get(id=pk)
    city.delete()
    return Response("City deleted succesfully !!")