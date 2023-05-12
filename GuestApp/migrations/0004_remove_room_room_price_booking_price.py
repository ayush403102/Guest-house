# Generated by Django 4.2 on 2023-05-10 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GuestApp', '0003_guest_guest_type_alter_room_room_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='room_price',
        ),
        migrations.AddField(
            model_name='booking',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]