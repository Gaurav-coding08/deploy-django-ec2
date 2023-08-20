from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET'])
def hi_message(request):
    hi_message= "Hi Bro"
    return Response(hi_message,status=200)

@api_view(['GET'])
def bye_message(request):
    bye_message= "Bye Bro"
    return Response(bye_message,status=200)
