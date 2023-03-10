# Generated by Django 4.1.5 on 2023-02-11 22:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_book_on_lending_item_on_lending_alter_book_edited_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='edited_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 11, 22, 28, 12, 266749, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='contact',
            name='edited_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 11, 22, 28, 12, 266050, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='item',
            name='edited_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 11, 22, 28, 12, 268222, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='lendingbook',
            name='edited_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 11, 22, 28, 12, 267412, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='lendingitem',
            name='edited_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 11, 22, 28, 12, 268907, tzinfo=datetime.timezone.utc)),
        ),
    ]
