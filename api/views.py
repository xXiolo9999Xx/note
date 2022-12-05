from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import note
from .segnializers import noteSerializers

# Create your views here.
@api_view(['GET'])
def getNotes(request):
    route = note.objects.all()
    serializers = noteSerializers(route, many = True)
    return Response(serializers.data)

@api_view(['GET'])
def getNote(request, pk):
    route = note.objects.get(id=pk)
    serializers = noteSerializers(route)
    return Response(serializers.data)

@api_view(['PUT'])
def updatedNote(request, pk):
    data = request.data
    Note = note.objects.get(id=pk)
    serializer = noteSerializers(instance= Note, data=data)
    
    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)

@api_view(['DELATE'])
def delatedNote(request,pk):
    Note = note.objects.get(id=pk)
    Note.delete()
    return Response('note deleted')
 
@api_view(['POST'])
def createNote(request):
    data = request.data
    Note = note.objects.create(
        body = data['body']
    )
    serializers = noteSerializers(Note,many=False)
    return Response(serializers.data)
    