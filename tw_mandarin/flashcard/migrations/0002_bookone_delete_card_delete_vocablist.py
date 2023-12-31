# Generated by Django 4.2.4 on 2023-08-04 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flashcard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookOne',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chinese', models.CharField(max_length=225)),
                ('pinyin', models.CharField(max_length=225)),
                ('english', models.CharField(max_length=225)),
                ('book', models.SmallIntegerField(default=1)),
                ('lesson', models.SmallIntegerField(default=None)),
                ('section', models.SmallIntegerField(default=None)),
            ],
        ),
        migrations.DeleteModel(
            name='Card',
        ),
        migrations.DeleteModel(
            name='VocabList',
        ),
    ]
