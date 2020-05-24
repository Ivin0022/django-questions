from django.db import models
from django.contrib.auth import get_user_model


class MultipleChoice(models.Model):
    """Model definition for MultipleChoice."""

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    question = models.ManyToManyField('MultipleChoiceQuestion')
    choice_text = models.CharField(max_length=50)

    class Meta:
        """Meta definition for MultipleChoice."""

        verbose_name = 'Multiple Choice'
        verbose_name_plural = 'Multiple Choices'

    def __str__(self):
        """Unicode representation of MultipleChoice."""
        return f'{self.choice_text}'
