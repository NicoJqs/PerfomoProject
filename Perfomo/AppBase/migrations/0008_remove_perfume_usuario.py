# Generated by Django 4.2.3 on 2023-09-12 23:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppBase', '0007_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perfume',
            name='usuario',
        ),
    ]