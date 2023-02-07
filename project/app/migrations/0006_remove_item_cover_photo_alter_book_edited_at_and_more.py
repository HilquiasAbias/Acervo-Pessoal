# Generated by Django 4.1.5 on 2023-02-07 12:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_remove_book_cover_photo_alter_book_edited_at_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='cover_photo',
        ),
        migrations.AlterField(
            model_name='book',
            name='edited_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 7, 12, 43, 21, 982337, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='contact',
            name='edited_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 7, 12, 43, 21, 982337, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='item',
            name='edited_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 7, 12, 43, 21, 982337, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='lendingbook',
            name='edited_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 7, 12, 43, 21, 982337, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='lendingitem',
            name='edited_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 7, 12, 43, 21, 982337, tzinfo=datetime.timezone.utc)),
        ),
    ]
