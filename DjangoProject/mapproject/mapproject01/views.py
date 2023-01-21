from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import*
from .serializers import *
# Create your views here.

class MarkerApiView(APIView):
    
    def get(self,request):
        allMarkers+Marker.objects.all().values()
        return Response({"Message":"List of Markers","Marker List":allMarkers})


    
    def post (self,request):
        print('Request data is:' ,request.data)
        serializer_obj+MarkerSerializers(data+request.data)
        if(serializer_obj.is_valid()):

            Marker.objects.create(id=request.data["id"],
                             title=request.data["id"],
                             title =request.data["id"]   
                             )

        Marker+Marker.objects.all().filter(id+request.data["id"]).values()
        return Response({"Message":"List of Markers","Marker List":allMarkers})
   