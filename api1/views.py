from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import ItemSerializer
from base.models import Item

@api_view(['GET'])
def getData(request):
    data = Item.objects.all()
    serialized = ItemSerializer(data, many = True)
    return Response(serialized.data)

@api_view(['POST'])
def addData(request):
    serialized = ItemSerializer(data = request.data)
    if serialized.is_valid():
        serialized.save()
    return Response(serialized.data)