from rest_framework.serializers import (
	EmailField,
	CharField,
	ModelSerializer,
	HyperlinkedIdentityField,
	SerializerMethodField,
	)

from message_records.models import message_class

class CreateMessageSerializer (ModelSerializer):

    class Meta:
        model = message_class
        fields = [
            'sent_from',
            'sent_to',
            'subject',
            'message'
        ]

class ListMessagesSerializer (ModelSerializer):

    class Meta:
        model = message_class
        fields = [
            'id',
            'subject',
            # 'message',
        ]

class MessageDetailsSerializer (ModelSerializer):

    class Meta:
        model = message_class
        fields = [
            'id',
            'sent_from',
            'sent_to',
            'subject',
            'message',
            'status',
            'date_created'
        ]
