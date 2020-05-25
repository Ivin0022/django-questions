from rest_framework import serializers

# local
from ..models import TextAnswer


class TextAnswerSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = TextAnswer
        fields = (
            'user',
            'question',
            'answer',
        )
