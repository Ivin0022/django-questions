from rest_framework import serializers

# local
from ..models import Question


class QuestionSerializer(serializers.Serializer):

    class Meta:
        model = Question
        fields = (
            'title_text',
            'choice_set',
        )