from django.conf.urls import url
from .views import message_board, MessageImformation

urlpatterns = [

    url(r'^$', message_board, name='message_board'),
    url(r'message_imformation/', MessageImformation.as_view()),

]
