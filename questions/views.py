from rest_framework import viewsets

# local
from .serializers import SectionSerializer
from .models import Section


class SectionViewset(viewsets.ModelViewSet):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer