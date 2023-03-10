# Generated by Django 4.1.5 on 2023-02-11 22:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_alter_book_edited_at_alter_contact_edited_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='on_lending',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='item',
            name='on_lending',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='book',
            name='edited_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 11, 22, 22, 38, 716487, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='contact',
            name='edited_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 11, 22, 22, 38, 715734, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='item',
            name='edited_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 11, 22, 22, 38, 717964, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='lendingbook',
            name='edited_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 11, 22, 22, 38, 717145, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='lendingitem',
            name='edited_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 11, 22, 22, 38, 718602, tzinfo=datetime.timezone.utc)),
        ),
    ]
