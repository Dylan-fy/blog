from django.conf.urls import url
from .views import message_board

urlpatterns = [

    url('', message_board, name='message_board'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
