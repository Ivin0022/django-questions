# -*- coding: utf-8 -*-
from django.contrib import admin

from ..models import TextQuestion


@admin.register(TextQuestion)
class TextQuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title_text')
    list_display_links = ('title_text',)
