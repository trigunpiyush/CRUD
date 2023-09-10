from rest_framework import generics, status, permissions
from rest_framework.response import Response
from .models import CuboidBox
from .serializers import (
    CuboidBoxCreateSerializer,
    CuboidBoxUpdateSerializer,
    CuboidBoxListSerializer,
    BoxSerializer
)
from django_filters.rest_framework import DjangoFilterBackend
from .filters import CuboidBoxFilter
from rest_framework import generics, serializers
from .models import CuboidBox
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from inventory.serializers import BoxSerializer

class UserBoxListView(generics.ListAPIView):
    serializer_class = BoxSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return CuboidBox.objects.filter(creator=user)



class CuboidBoxCreateView(generics.CreateAPIView):
    serializer_class = CuboidBoxCreateSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

class CuboidBoxUpdateView(generics.UpdateAPIView):
    queryset = CuboidBox.objects.all()
    serializer_class = CuboidBoxUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        # Prevent updates to 'creator' and 'created_at' fields
        serializer.validated_data.pop('creator', None)
        serializer.validated_data.pop('created_at', None)
        serializer.save()

class CuboidBoxListView(generics.ListAPIView):
    serializer_class = CuboidBoxListSerializer
    #filter_backends = [DjangoFilterBackend]
    filterset_class = CuboidBoxFilter

    def get_queryset(self):
        queryset = CuboidBox.objects.all()
        
        # Restrict access to staff users only for their created boxes
        if self.request.user.is_staff:
            return queryset
        else:
            return queryset.filter(creator=self.request.user)

class CuboidBoxDeleteView(generics.DestroyAPIView):
    queryset = CuboidBox.objects.all()
    serializer_class = CuboidBoxListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_destroy(self, instance):
        if instance.creator == self.request.user:
            instance.delete()
        else:
            return Response({'message': 'You do not have permission to delete this box.'}, status=status.HTTP_403_FORBIDDEN)
