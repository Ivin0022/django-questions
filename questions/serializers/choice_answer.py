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

    def create(self, validated_data):
        answer, created = ChoiceAnswer.objects.update_or_create(
            question=validated_data.get('question'),
            user=validated_data.get('user'),
            defaults={'answer': validated_data.get('answer')}
        )
        return answer