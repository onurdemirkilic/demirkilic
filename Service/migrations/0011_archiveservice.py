# Generated by Django 4.2.3 on 2023-07-28 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Service', '0010_intelligenceservice_top_secret_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArchiveService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=66)),
                ('file', models.FileField(upload_to='')),
            ],
        ),
    ]