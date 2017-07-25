from django.db import models


class MessageBoard(models.Model):
    '''用户匿名或创名留言'''
    visitor_name = models.CharField(max_length=30, help_text='访客姓名')
    visitor_message = models.TextField(help_text='访客留言')
    message_create_at = models.DateField(auto_now_add=True, help_text='留言时间')

    def __str__(self):
        return "%s:%s" % (visitor_name, message_create_at)
