from django.db import models
from django.contrib.auth import get_user_model


class TextAnswer(models.Model):
    """Model definition for TextAnswer."""

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    question = models.ForeignKey('TextQuestion', on_delete=models.CASCADE)
    answer = models.CharField('Answer', max_length=100)

    class Meta:
        """Meta definition for TextAnswer."""

        verbose_name = 'Text Answer'
        verbose_name_plural = 'Text Answers'

    def __str__(self):
        """Unicode representation of TextAnswer."""
        return f'{self.answer}'