# Generated by Django 4.1.1 on 2022-10-19 06:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_alter_tb_1_options_tb_1__time'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tb_1',
            options={'ordering': ['-_time'], 'verbose_name': '用戶資料庫', 'verbose_name_plural': '用戶資料庫'},
        ),
    ]
