# Generated by Django 4.2.3 on 2023-12-27 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Service', '0019_alter_archiveservice_code_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='archiveservice',
            name='code',
            field=models.CharField(default='G88242', max_length=100),
        ),
        migrations.AlterField(
            model_name='intelligenceservice',
            name='code',
            field=models.CharField(default='C95397', max_length=100),
        ),
    ]
