# Generated by Django 2.2.7 on 2020-05-25 13:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0005_section'),
    ]

    operations = [
        migrations.RenameField(
            model_name='section',
            old_name='Title',
            new_name='title',
        ),
    ]