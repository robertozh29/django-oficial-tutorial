# Generated by Django 5.1.5 on 2025-01-17 01:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='publication_date',
            new_name='pub_date',
        ),
    ]
