from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout
from rest_framework.authtoken.models import Token
from django.shortcuts import redirect
from rest_framework.permissions import IsAuthenticated


class UserRegistrationApiView(APIView):
    serializer_class = serializers.UserRegistrationSerializer
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            user = serializer.save()
            return Response("User registered")
        
        return Response(serializer.errors)
    
class UserLoginApiView(APIView):
    def post(self, request):
        serializer = serializers.UserLoginSerializer(data = self.request.data)
        
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            user = authenticate(username=username, password=password)
            
            if user:
                token, _ = Token.objects.get_or_create(user=user)
                print("=========================")
                print(token)
                print("=========================")
                print(_)
                login(request, user)
                return Response({'token' : token.key, 'user_id' : user.id})
            else:
                return Response({'error' : "Invalid Credential"})
            
        return Response(serializer.errors)

# class UserLogoutApiView(APIView):
#     def get(self, request):
#         request.user.auth_token.delete()
#         logout(request)
#         return redirect('login')

class UserLogoutApiView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        
        try:
            token = Token.objects.get(user=request.user)
            token.delete()
        except Token.DoesNotExist:
            pass  
        
        logout(request)
        return Response("User logged out")