from rest_framework import viewsets

# local
from .serializers import SectionSerializer
from .models import Section


class SectionViewset(viewsets.ReadOnlyModelViewSet):
    queryset = Section.objects.filter(level=0)
    serializer_class = SectionSerializer