from django.contrib import admin
from django.utils.html import format_html

# 3rd party
from feincms.admin import tree_editor
from adminsortable2.admin import SortableInlineAdminMixin

# local
from ..models import Section


@admin.register(Section)
class SectionAdmin(tree_editor.TreeEditor):
    '''Admin View for Section'''
    list_display = ('__str__',)
    # active_toggle = tree_editor.ajax_editable_boolean('hidden', 'hidden')
    # inlines = [
    #     SubCategoryInline,
    #     CategoryImageInline,
    #     ProductInline,
    # ]
    search_fields = ('title',)
