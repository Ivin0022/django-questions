from django.contrib import admin
from django.utils.html import format_html

# 3rd party
from feincms.admin import tree_editor
from adminsortable2.admin import SortableInlineAdminMixin

# local
from ..models import Section, Question


class QuestionInline(SortableInlineAdminMixin, admin.TabularInline):
    '''Tabular Inline View for Question'''
    fields = (
        'title_text',
        'type',
    )
    model = Question
    min_num = 0
    max_num = 10
    extra = 1
    show_change_link = True


@admin.register(Section)
class SectionAdmin(tree_editor.TreeEditor):
    '''Admin View for Section'''
    list_display = ('__str__',)
    # active_toggle = tree_editor.ajax_editable_boolean('hidden', 'hidden')
    inlines = [
        QuestionInline,
    ]
    search_fields = ('title',)
