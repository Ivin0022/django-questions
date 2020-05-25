from django.db import models


class Question(models.Model):
    """Model definition for Question."""

    TEXT = 't'
    DROPDOWN = 'd'
    RADIO = 'r'
    CHECKBOX = 'c'

    TYPE_CHOICE = (
        (TEXT, 'text'),
        (DROPDOWN, 'dropdown'),
        (RADIO, 'radio'),
        (CHECKBOX, 'checkbox'),
    )

    title_text = models.CharField('Question Title', max_length=100)
    type = models.CharField(
        'question type',
        max_length=1,
        choices=TYPE_CHOICE,
        help_text='select type of question'
        'for dropdown, radio, checkbox'
        'add a the choice below',
    )

    class Meta:
        """Meta definition for Question."""

        verbose_name = 'Question'
        verbose_name_plural = 'Questions'

    def __str__(self):
        """Unicode representation of Question."""
        return f'{self.title_text}'
