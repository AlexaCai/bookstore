# Generated by Django 4.2.6 on 2023-11-07 15:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sale',
            old_name='book',
            new_name='book_name',
        ),
    ]
