# Generated by Django 2.2.24 on 2023-12-06 18:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0021_auto_20231128_0149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='claim',
            name='flat_number',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='flat_complaints', to='property.Flat', verbose_name='Номер квартиры'),
        ),
        migrations.AlterField(
            model_name='claim',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='claims_user', to=settings.AUTH_USER_MODEL, verbose_name='Кто жаловался?'),
        ),
    ]