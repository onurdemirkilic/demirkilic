# Generated by Django 4.2.3 on 2023-07-28 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Service', '0009_intelligenceservice'),
    ]

    operations = [
        migrations.AddField(
            model_name='intelligenceservice',
            name='TOP_SECRET',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='intelligenceservice',
            name='business_adress',
            field=models.CharField(max_length=9999),
        ),
        migrations.AlterField(
            model_name='intelligenceservice',
            name='home_adress',
            field=models.CharField(max_length=9999),
        ),
        migrations.AlterField(
            model_name='intelligenceservice',
            name='phone_number',
            field=models.CharField(max_length=9999),
        ),
    ]
