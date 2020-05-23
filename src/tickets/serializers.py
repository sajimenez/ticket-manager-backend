from rest_framework import serializers

from .models import Ticket


class TicketSerializer(serializers.ModelSerializer):
    creator = serializers.StringRelatedField()

    class Meta:
        model = Ticket
        fields = ['id', 'title', 'description', 'status', 'created', 'creator']
        read_only_fields = ['id', 'created', 'creator']
