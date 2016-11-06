import jwt  # Requires: pip install python-jwt
import Crypto.PublicKey.RSA as RSA  # Requires: pip install pycrypto
from django.contrib.auth import user_logged_in, user_logged_out
import datetime
from rest_framework import response, status, authtoken
import firebasetoken

# Get your service account's email address and private key from the JSON key file


def login_user(request, user):
    token, _ = authtoken.models.Token.objects.get_or_create(user=user)
    firebase_token = firebasetoken.models.FirebaseToken.objects.create(user=user)
    user_logged_in.send(sender=user.__class__, request=request, user=user)
    return token, firebase_token

def logout_user(request):
    authtoken.models.Token.objects.filter(user=request.user).delete()
    firebasetoken.models.FirebaseToken.objects.filter(user=request.user).delete()
    user_logged_out.send(sender=request.user.__class__, request=request, user=request.user)