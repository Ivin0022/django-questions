from django.db import models


class MultipleChoiceQuestion(models.Model):
    """Model definition for MultipleChoiceQuestion."""

    title_text = models.CharField('Question Title', max_length=100)

    class Meta:
        """Meta definition for MultipleChoiceQuestion."""

        verbose_name = 'Multiple Choice Question'
        verbose_name_plural = 'Multiple Choice Questions'

    def __str__(self):
        """Unicode representation of MultipleChoiceQuestion."""
        return f'{self.title_text}'
