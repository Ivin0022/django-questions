from rest_framework import viewsets
from rest_framework import mixins

# local
from .serializers import (
    SectionSerializer,
    TextAnswerSerializer,
    ChoiceAnswerSerializer,
    MultipleChoiceAnswerSerializer,
)
from .models import (
    Section,
    TextAnswer,
    ChoiceAnswer,
    MultipleChoiceAnswer,
)


class SectionViewset(viewsets.ReadOnlyModelViewSet):
    queryset = Section.objects.filter(level=0)
    serializer_class = SectionSerializer


class TextAnswerViewset(viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.UpdateModelMixin):
    queryset = TextAnswer.objects.all()
    serializer_class = TextAnswerSerializer


class ChoiceAnswerViewset(viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.UpdateModelMixin):
    queryset = ChoiceAnswer.objects.all()
    serializer_class = ChoiceAnswerSerializer


class MultipleChoiceAnswerViewset(viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.UpdateModelMixin):
    queryset = MultipleChoiceAnswer.objects.all()
    serializer_class = MultipleChoiceAnswerSerializer