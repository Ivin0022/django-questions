# -*- coding: utf-8 -*-
from django.contrib import admin
from django.db import models
from django.forms import CheckboxSelectMultiple

from ..models import MultipleChoiceAnswer


@admin.register(MultipleChoiceAnswer)
class MultipleChoiceAnswerAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'question')
    list_display_links = ('user',)
    list_filter = ('user', 'question', 'answer')
    formfield_overrides = {
        models.ManyToManyField: {
            'widget': CheckboxSelectMultiple
        },
    }