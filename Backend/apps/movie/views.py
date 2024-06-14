from django.shortcuts import render
from rest_framework.views import APIView
from .serializer import ReviewSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import Review
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class moviee(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data
        serializer = ReviewSerializer(data = data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, pk=None):

        if pk:
            try:
                data = Review.objects.get(id = pk)
                serializer = ReviewSerializer(data)
                return Response(serializer.data)
            except Review.DoesNotExist:
                return Response(serializer.errors)
        else:
            data = Review.objects.all()
            serializer = ReviewSerializer(data, many = True)
            return Response(serializer.data)
        
    def delete(self, request, pk):

        try:
            data = Review.objects.get(id = pk)
            data.delete()
            return Response({'message':'successfully deleted'})
        except Review.DoesNotExist:
            return Response({'message' : 'not such movie exists in database'})
        
    def patch(self, request, pk):
        try:
            data = Review.objects.get(id = pk)
            serializer = ReviewSerializer(instance=data , data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Review.DoesNotExist:
            return Response({'message':'does not exists, cant patch'})
        
        

        

    

