import json
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404, HttpResponse

from pythontest.ApiUnit.serializers import ApiDataSerializer
from pythontest.libs.libclient import Minion


# Create your views here.
class MasterServerView(APIView):
    def get(self, request):
        print('This is api GET method!')
        serializer = ApiDataSerializer()
        print(serializer)

        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        print('This is api POST method!')
        serializer = ApiDataSerializer(data=request.data)

        # print(serializer)

        if serializer.is_valid():
            command = serializer.data.get('command')
            print('command: {0} ' . format(command))
            if command is None:
                return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)

            result = dict()

            # Send command to server
            message = serializer.data.get('message', None)
            if message is None or len(message) <= 0:
                result['errorMessage'] = 'Can not get message, please check it!'
                return Response(result, status=status.HTTP_400_BAD_REQUEST)

            try:
                client = Minion()
                client.set_message(message)
                result['result'] = client.run()
            except:
                result['errorMessage'] = 'Can not send data to master server!'
                return Response(result, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            print(result)

            return Response(result, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)