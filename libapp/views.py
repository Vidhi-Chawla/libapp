from rest_framework import viewsets
from rest_framework import generics
from django.shortcuts import get_object_or_404
from . import models
from . import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class BookViewSet(APIView):
    def get(self, request, id=None):
        if id:
            item = get_object_or_404(models.Books, id=id)
            serializer = serializers.BookSerializer(item)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        items = models.Books.objects.all()
        serializer = serializers.BookSerializer(items, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = serializers.BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    

    def delete(self, request, id=None):
        item = get_object_or_404(models.Books, id=id)
        item.delete()
        return Response({"status": "success", "data": "Item Deleted"}, status=status.HTTP_204_NO_CONTENT)

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=serializers.BookSerializer
    queryset=models.Books.objects.all()

class BookSelectView(APIView):
    def get(self, request):
        title_query = request.query_params.get('title', None)
        if title_query:
            books = models.Books.objects.filter(title__icontains=title_query)
        else:
            books = models.Books.objects.all()
        serializer = serializers.BookSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)