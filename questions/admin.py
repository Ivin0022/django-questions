# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import TextQuestion, TextAnswer


@admin.register(TextQuestion)
class TextQuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title_text')
    list_display_links = ('title_text',)


@admin.register(TextAnswer)
class TextAnswerAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'question', 'answer')
    list_filter = ('user', 'question')
