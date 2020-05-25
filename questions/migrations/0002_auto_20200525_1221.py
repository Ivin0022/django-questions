# Generated by Django 2.2.7 on 2020-05-25 12:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='question',
            options={'verbose_name': 'Question', 'verbose_name_plural': 'Questions'},
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=100, verbose_name='choice text')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.Question')),
            ],
            options={
                'verbose_name': 'Choice',
                'verbose_name_plural': 'Choices',
            },
        ),
    ]