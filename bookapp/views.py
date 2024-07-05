from rest_framework import viewsets
from .models import User, Book, Transaction
from rest_framework import generics
from .serializers import UserSerializer, BookSerializer, TransactionSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=UserSerializer
    queryset=User.objects.all()

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=BookSerializer
    queryset=Book.objects.all()

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

class TransactionDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=TransactionSerializer
    queryset=Transaction.objects.all()
