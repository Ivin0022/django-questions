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

    def create(self, validated_data):
        answer, created = TextAnswer.objects.update_or_create(
            question=validated_data.get('question'),
            user=validated_data.get('user'),
            defaults={'answer': validated_data.get('answer')}
        )
        return answer