# Generated by Django 4.2 on 2023-05-10 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GuestApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Img',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default=None, null=True, upload_to='img/')),
            ],
        ),
    ]