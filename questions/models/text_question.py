from django.db import models


class TextQuestion(models.Model):
    """Model definition for TextQuestion."""

    title_text = models.CharField('Question Title', max_length=100)

    class Meta:
        """Meta definition for TextQuestion."""

        verbose_name = 'Text Question'
        verbose_name_plural = 'Text Questions'

    def __str__(self):
        """Unicode representation of TextQuestion."""
        return f'{self.title_text}'
