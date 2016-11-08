from django.shortcuts import render

# Create your views here.
from rest_framework import views
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser, MultiPartParser
from faces.serializers import FacesSerializer

import cv2
import urllib
from faces.utils import get_image

class FacesView(views.APIView):
    permission_classes = []
    #parser_classes = (FileUploadParser,)
    serializer_class = FacesSerializer

    def put(self, request, *args, **kwargs):
        cascPath = urllib.urlretrieve("https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_frontalface_default.xml")[0]
        faceCascade = cv2.CascadeClassifier(cascPath)
        window = 40
        url = request.POST.get("url", None)        
        if window and url:
            image = get_image(url)
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            # Detect faces in the image
            faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(window, window),
            flags = cv2.cv.CV_HAAR_SCALE_IMAGE
            )

            return Response({"count": len(faces)})
        else:
            return Response({"count": "unknown"})
            