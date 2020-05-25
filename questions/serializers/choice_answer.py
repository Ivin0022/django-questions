from rest_framework import serializers

# local
from ..models import ChoiceAnswer


class ChoiceAnswerSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = ChoiceAnswer
        fields = (
            'user',
            'question',
            'answer',
        )
