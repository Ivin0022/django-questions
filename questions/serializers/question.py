from rest_framework import serializers

# local
from ..models import Question
from .choice import ChoiceSerializer


class QuestionSerializer(serializers.ModelSerializer):
    choice_set = ChoiceSerializer(many=True)

    class Meta:
        model = Question
        fields = (
            'id',
            'title_text',
            'type',
            'choice_set',
        )
