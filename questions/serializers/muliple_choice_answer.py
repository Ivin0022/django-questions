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

    def create(self, validated_data):
        answer, created = MultipleChoiceAnswer.objects.update_or_create(
            question=validated_data.get('question'),
            user=validated_data.get('user'),
            defaults={},
        )
        answer.answer.set(validated_data.get('answer'))
        return answer