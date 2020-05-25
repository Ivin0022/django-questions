from rest_framework import serializers

# local
from ..models import Choice


class ChoiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Choice
        fields = (
            'id',
            'choice_text',
        )
