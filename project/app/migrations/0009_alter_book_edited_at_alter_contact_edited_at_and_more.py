# Generated by Django 4.1.5 on 2023-02-11 14:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_book_edited_at_alter_contact_edited_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='edited_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 11, 14, 22, 19, 555795, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='contact',
            name='edited_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 11, 14, 22, 19, 555091, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='item',
            name='edited_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 11, 14, 22, 19, 557270, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='lendingbook',
            name='edited_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 11, 14, 22, 19, 556437, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='lendingitem',
            name='edited_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 11, 14, 22, 19, 557902, tzinfo=datetime.timezone.utc)),
        ),
    ]