from rest_framework.response import Response 
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view

from aws_services.services import KinesisVideoStream as kvs

# Create your views here.
class consumerView(APIView):
    @api_view(('POST', ))
    def open_signaling_channel(req):
        params = req.data 
        channel_name = params['channel_name']
        response = kvs(channel_name).create_channel()
        if(response):
            response = {"response":"the channel is successfully created"}
            return Response(data=response, status=status.HTTP_201_CREATED)

