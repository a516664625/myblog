# Generated by Django 2.1 on 2020-03-26 18:41

import DjangoUeditor.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=DjangoUeditor.models.UEditorField(default='', verbose_name='内容'),
        ),
    ]
