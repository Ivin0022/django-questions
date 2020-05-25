from rest_framework import serializers

# djangorestframework-recursive
from rest_framework_recursive.fields import RecursiveField

# local
from .question import QuestionSerializer
from ..models import Section


class SectionSerializer(serializers.ModelSerializer):
    children = RecursiveField(required=False, allow_null=True, many=True)
    question_set = QuestionSerializer(many=True)

    class Meta:
        model = Section
        fields = (
            'id',
            'url',
            'title',
            'parent',
            'question_set',
            'children',
        )
