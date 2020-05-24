from django.db import models


class ChoiceQuestion(models.Model):
    """Model definition for ChoiceQuestion."""

    title_text = models.CharField('Question Text', max_length=100)

    class Meta:
        """Meta definition for ChoiceQuestion."""

        verbose_name = 'Choice Question'
        verbose_name_plural = 'Choice Questions'

    def __str__(self):
        """Unicode representation of ChoiceQuestion."""
        return f'{self.title_text}'
