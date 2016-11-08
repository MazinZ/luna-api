from django.shortcuts import render
from firebasetoken.serializers import *
from users.utils import login_user, logout_user, delete_user
from djoser.utils import ActionViewMixin
from rest_framework import generics, permissions, status, response, views
from djoser import serializers
from rest_framework.response import Response
import djoser.views

# Create your views here.

class FirebaseLoginView(djoser.views.LoginView):
    """
    Use this endpoint to obtain user authentication token and Firebase token.
    """
    serializer_class = serializers.serializers_manager.get('login')
    permission_classes = (
        permissions.AllowAny,
    )

    def action(self, serializer):
        token, firebasetoken = login_user(self.request, serializer.user)
        token_serializer_class = serializers.serializers_manager.get('token')
        firebasetoken_serializer_class = FirebaseTokenSerializer

        #print [token_serializer_class(token).data, firebasetoken_serializer_class(firebasetoken).data]

        return response.Response({
        'auth_token': token_serializer_class(token).data,
        'firebase_token': firebasetoken_serializer_class(firebasetoken).data,
         },
            status=status.HTTP_200_OK,
        )


class FirebaseLogoutView(djoser.views.LogoutView):
    """
    Use this endpoint to logout user (remove user authentication and Firebase tokens).
    """
    permission_classes = (
        permissions.IsAuthenticated,
    )

    def post(self, request):
        logout_user(request)
        return response.Response(status=status.HTTP_204_NO_CONTENT)

class DeleteUserView(views.APIView):
    """
    Use this endpoint to delete a user. Note: you should also delete the user from Firebase manually.
    """
    permission_classes = (
        permissions.IsAuthenticated,
    )

    def post(self, request):
        delete_user(request)
        return response.Response(status=status.HTTP_204_NO_CONTENT)