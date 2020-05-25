from rest_framework import serializers

# local
from ..models import MultipleChoiceAnswer


class MultipleChoiceAnswerSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = MultipleChoiceAnswer
        fields = (
            'user',
            'question',
            'answer',
        )
