from django.shortcuts import render
from firebasetoken.serializers import *
from users.utils import login_user, logout_user, delete_user, flattenjson
from djoser.utils import ActionViewMixin
from rest_framework import generics, permissions, status, response, views
from djoser import serializers
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
import djoser.views
import time, csv
from users.serializers import ExportSerializer
from django.http import HttpResponse


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


class GenerateFileOutputView(views.APIView):
    """
    This endpoint is used to generate an output file given JSON from the Firebase database
    """
    serializer_class = ExportSerializer
    permission_class = (
        #permissions.IsAdminUser,
        #permissions.IsAuthenticated,
    )
    def post(self, request):
        response = HttpResponse(content_type='text/csv')
        input = []
        content = request.body
        json_input = json.loads(content)
        json_input = json_input['content']

        for i in json_input:
            input.append(json_input[i])
        

        input = map( lambda x: flattenjson( x, "__" ), input)
        columns = map( lambda x: x.keys(), input )
        columns = reduce( lambda x,y: x+y, columns )
        columns = list( set( columns ) )
        f = csv.writer(response)
        f.writerow(columns)

        for i_r in input:
            f.writerow( map( lambda x: i_r.get( x, "" ), columns ) )
        current_time = time.strftime("%Y/%m/%d")
        response['Content-Disposition'] = 'attachment; filename="data_' + current_time + '.csv"'
        return response

