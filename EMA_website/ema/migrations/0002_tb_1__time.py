# Generated by Django 4.1.1 on 2022-10-27 07:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ema', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tb_1',
            name='_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
