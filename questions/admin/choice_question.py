# -*- coding: utf-8 -*-
from django.contrib import admin

from ..models import ChoiceQuestion, Choice


class ChoiceInline(admin.TabularInline):
    '''Tabular Inline View for Choice'''

    model = Choice
    min_num = 1
    max_num = 10
    extra = 0


@admin.register(ChoiceQuestion)
class ChoiceQuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title_text')
    list_display_links = ('title_text',)
    inlines = [ChoiceInline]