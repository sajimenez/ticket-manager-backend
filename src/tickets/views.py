from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions

from .serializers import TicketSerializer
from .models import Ticket


class ListCreateTicketAPIView(generics.ListCreateAPIView):
    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]

    def get_queryset(self):
        queryset = Ticket.objects.all()
        status = self.request.query_params.get('status', None)
        if status:
            return queryset.filter(status=status)
        return queryset

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class RetrieveUpdateTicketAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]
    queryset = Ticket.objects.all()
