# Generated by Django 2.2 on 2020-07-20 14:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20200720_1459'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='Author',
        ),
    ]
