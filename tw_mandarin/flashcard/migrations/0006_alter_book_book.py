# Generated by Django 4.2.4 on 2023-08-09 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flashcard', '0005_rename_bookone_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book',
            field=models.SmallIntegerField(default=None),
        ),
    ]
