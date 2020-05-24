# Generated by Django 2.2.7 on 2020-05-24 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0004_choiceanswer'),
    ]

    operations = [
        migrations.CreateModel(
            name='MultipleChoiceQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_text', models.CharField(max_length=100, verbose_name='Question Title')),
            ],
            options={
                'verbose_name': 'MultipleChoiceQuestion',
                'verbose_name_plural': 'MultipleChoiceQuestions',
            },
        ),
    ]
