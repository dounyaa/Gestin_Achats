# Generated by Django 4.1.4 on 2023-01-13 09:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GestionAchats', '0003_command'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='first_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='client',
            name='last_name',
        ),
    ]