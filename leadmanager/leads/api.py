from leads.models import Lead
from rest_framework import viewsets, permissions
from .serializers import LeadSerializer

#Lead Viewset
class LeadViewSet(viewsets.ModelViewSet):
  serializer_class = LeadSerializer
  permission_classes = [
      permissions.AllowAny
  ]
  queryset = Lead.objects.all()
