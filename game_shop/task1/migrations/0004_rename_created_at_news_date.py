# Generated by Django 5.1.2 on 2024-12-17 04:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task1', '0003_news'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='created_at',
            new_name='date',
        ),
    ]
