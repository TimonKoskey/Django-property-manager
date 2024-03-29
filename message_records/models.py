from django.db import models
from app_users.models import user_detail_class
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

class Message (models.Model):
    sent_from = models.ForeignKey (user_detail_class , related_name='sender_details', on_delete=models.CASCADE)
    sent_to = models.ForeignKey (user_detail_class , related_name='receiver_details', on_delete=models.CASCADE)
    subject = models.CharField(max_length=30)
    message = models.CharField(max_length=500)
    status = models.CharField(max_length=20)
    date_created = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(null=True)
    object_id = models.PositiveIntegerField(null=True,blank=True)
    content_type = models.ForeignKey(ContentType,on_delete = models.CASCADE,null=True,blank=True)
    content_object = GenericForeignKey('content_type', 'object_id')

message_class = Message
