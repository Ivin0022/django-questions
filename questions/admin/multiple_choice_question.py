# -*- coding: utf-8 -*-
from django.contrib import admin

from ..models import MultipleChoiceQuestion, MultipleChoice


@admin.register(MultipleChoiceQuestion)
class MultipleChoiceQuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title_text')
