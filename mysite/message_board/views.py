from django.shortcuts import render
from .models import MessageBoard


def message_board(request):
    return render(request, 'message_board.html')


def message_imformation(request):
    pass
