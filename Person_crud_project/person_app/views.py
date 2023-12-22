
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Person
from .serializers import MyAppSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated


@api_view(http_method_names=['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def create_person(request):
    try:
        serializer = MyAppSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    except Exception as e:
        return Response(data=serializer.errors)

    # if request.method == 'GET':
    #     person = Person.objects.all()
    #     serializer = MyAppSerializer(person, many=True)
    #     return Response(serializer.data, )
    

@api_view()
def show_person(request):
    try:
        persons = Person.objects.all()
        serializer = MyAppSerializer(persons, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response(data={'detail':'Error fetching data'}, status=status.HTTP_400_BAD_REQUEST)
    

@api_view()
def retrive_person(request, pk=None):
    try:
        person = get_object_or_404(Person, pk=pk)
        serializer = MyAppSerializer(person)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response(data={'detail':'Error retriving data'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(http_method_names=['PUT','PATCH'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def update_person(request, pk=None):
    try:
        person = get_object_or_404(Person, pk=pk)
        if request.method == 'PUT':
            serializer = MyAppSerializer(data=request.data, instance=person)
        if request.method == 'PATCH':
            serializer = MyAppSerializer(data=request.data, instance=person)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response(data={'detail':'Error updating data'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(http_method_names=['DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def delete_person(request, pk=None):
    try:
        person = get_object_or_404(Person, pk=pk)
        person.delete()
        return Response(data={'deatils':'Person deleted successfully'}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response(data={'detail':'Error deleting data'}, status=status.HTTP_400_BAD_REQUEST)




