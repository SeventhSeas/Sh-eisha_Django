# Generated by Django 2.1.5 on 2022-09-28 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20220927_1732'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='choice_text',
        ),
        migrations.AddField(
            model_name='comment',
            name='body',
            field=models.TextField(blank=True, null=True),
        ),
    ]
