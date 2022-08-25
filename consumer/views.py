from rest_framework.response import Response 
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view

from aws_services.services import KinesisVideoStream as kvs

# Create your views here.
class consumerView(APIView):
    @api_view(('POST', ))
    def create_signaling_channel(req):
        params = req.data 
        channel_name = params['channel_name']
        res = kvs(channel_name).create_channel()
        if(res):
            res = {"response":"the channel is successfully created"}
            return Response(data=res, status=status.HTTP_201_CREATED)

    @api_view(('POST', ))
    def delete_signaling_channel(req):
        params = req.data 
        channel_name = params['channel_name']
        res = kvs(channel_name).delete_channel()
        if(res):
            res = {"response":"the channel is successfully deleted"}
            return Response(data=res, status=status.HTTP_200_OK)
        else:
            res = {"response":"this channel does not exists!"}
            return Response(data=res)
