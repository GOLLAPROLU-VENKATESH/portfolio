# Generated by Django 3.2.4 on 2021-06-14 16:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='url',
            new_name='purl',
        ),
    ]