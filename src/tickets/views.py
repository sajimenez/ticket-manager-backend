from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions

from .serializers import TicketSerializer
from .models import Ticket


class TicketViewSet(mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    mixins.UpdateModelMixin,
                    viewsets.GenericViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]

    def get_queryset(self):
        status = self.request.query_params.get('status', None)
        if status:
            return self.queryset.filter(status=status)
        return self.queryset

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)
