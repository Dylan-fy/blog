from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions

from .serializers import MessageBoardSerializer
from .models import MessageBoard


def message_board(request):
    return render(request, 'message_board.html')


class MessageImformation(APIView):

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get(self, request, format=None):
        messageboards = MessageBoard.objects.all()
        serializer = MessageBoardSerializer(messageboards, many=True)
        return Response(serializer.data)

    # def post(self, request, format=None):
    #     serializer = MessageBoardSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
