# Generated by Django 3.1.8 on 2021-04-12 14:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopee', '0005_buyer_md5'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='buyer',
            name='md5',
        ),
    ]
