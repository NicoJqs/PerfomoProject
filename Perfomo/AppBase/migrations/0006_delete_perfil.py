# Generated by Django 4.2.3 on 2023-09-12 21:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppBase', '0005_remove_perfil_linkgithub_remove_perfil_linklinkedin_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Perfil',
        ),
    ]
