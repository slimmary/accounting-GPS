# Generated by Django 2.2.4 on 2020-06-22 18:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0004_auto_20200424_1412'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehicle',
            name='owner',
        ),
    ]