# Generated by Django 2.2.24 on 2023-11-27 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0018_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='owner_name',
            field=models.CharField(db_index=True, max_length=200, verbose_name='ФИО владельца'),
        ),
    ]
