from django.shortcuts import render, HttpResponse, get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from fbv.models import People
from fbv.serializers import PeopleSerializer

# Create your views here.


def home(request):
    return HttpResponse('<h1>API Page</h1>')


@api_view(['GET', 'POST'])
def people_get_post(request):
    if request.method == "GET":
        person = People.objects.all()
        serializers = PeopleSerializer(person, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        serializers = PeopleSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            data = {
                "messages": f"{serializers.validated_data.get('first_name')} recorded successfully "
            }
            return Response(data, status=status.HTTP_201_CREATED)
    return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET","PUT","DELETE","PATCH"])
def people_put_delete_patch(request, pk):
    person = get_object_or_404(People, pk=pk)
    if request.method == "GET":
        serializer = PeopleSerializer(person)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "PUT":
        serializer = PeopleSerializer(person, data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": f"{person.last_name} updated successfully "
            }
            return Response(data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "PATCH":
        serializer = PeopleSerializer(person, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": f"{person.last_name} updated successfully "
            }
            return Response(data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        person.delete()
        data = {
            "message" : f"{person.last_name} was deleted "
        }
        return Response( data)
