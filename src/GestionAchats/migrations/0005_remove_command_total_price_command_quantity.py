# Generated by Django 4.1.4 on 2023-01-13 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GestionAchats', '0004_rename_first_name_client_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='command',
            name='total_price',
        ),
        migrations.AddField(
            model_name='command',
            name='quantity',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
