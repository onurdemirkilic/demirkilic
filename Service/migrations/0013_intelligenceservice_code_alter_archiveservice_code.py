# Generated by Django 4.2.3 on 2023-07-28 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Service', '0012_archiveservice_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='intelligenceservice',
            name='code',
            field=models.CharField(default='C67362', max_length=100),
        ),
        migrations.AlterField(
            model_name='archiveservice',
            name='code',
            field=models.CharField(default='E23259', max_length=100),
        ),
    ]
