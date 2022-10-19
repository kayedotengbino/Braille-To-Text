from django.http import JsonResponse
from .models import brailleTo
from .serializer import brailleSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def input_list(request):
    if request.method == 'GET':
        inputs = brailleTo.objects.all()
        serializer = brailleSerializer(inputs, many = True)
        return JsonResponse({"inputs": serializer.data})
    
    if request.method == 'POST':
        serializer = brailleSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)