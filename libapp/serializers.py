from rest_framework import serializers
from .models import Books
from django.contrib.auth.models import User

#class UserSerializer(serializers.ModelSerializer):
   # class Meta:
       # model = User
       # fields = ['id', 'username', 'email']

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'
