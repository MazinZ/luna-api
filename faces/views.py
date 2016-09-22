from django.shortcuts import render

# Create your views here.
from rest_framework import views
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser, MultiPartParser

"""import cv2
import urllib

class FacesView(views.APIView):
    permission_classes = []
    parser_classes = (FileUploadParser,)

    def put(self, request, *args, **kwargs):
        cascPath = urllib.urlretrieve("https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_frontalface_default.xml")[0]
        faceCascade = cv2.CascadeClassifier(cascPath)
        window = request.DATA.get('window', None)
        img = request.FILES['img']
        if window and img:
            #open(filename, 'wb+') as img:
            image = cv2.imread(img)
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            # Detect faces in the image
            faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(window, window),
            flags = cv2.cv.CV_HAAR_SCALE_IMAGE
            )

            print "Found {0} faces!".format(len(faces))

            # Draw a rectangle around the faces
            for (x, y, w, h) in faces:
                cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

                cv2.imshow("Faces found", image)
                cv2.waitKey(0)
            return Response({"count": len(faces)})
        else:
            return Response({"count": "unknown"})
            """