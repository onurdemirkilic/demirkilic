# Generated by Django 4.2.3 on 2023-07-28 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Service', '0011_archiveservice'),
    ]

    operations = [
        migrations.AddField(
            model_name='archiveservice',
            name='code',
            field=models.CharField(default='G83589', max_length=100),
        ),
    ]
