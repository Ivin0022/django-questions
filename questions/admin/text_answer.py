# -*- coding: utf-8 -*-
from django.contrib import admin

from ..models import TextAnswer


@admin.register(TextAnswer)
class TextAnswerAdmin(admin.ModelAdmin):
    list_display = ('id', 'answer', 'user', 'question')
    list_display_links = ('answer',)
    list_filter = ('user', 'question')
