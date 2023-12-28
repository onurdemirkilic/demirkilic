# Generated by Django 4.2.3 on 2023-07-28 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Service', '0008_ticketservice'),
    ]

    operations = [
        migrations.CreateModel(
            name='IntelligenceService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=66)),
                ('phone_number', models.TextField()),
                ('job', models.CharField(max_length=120)),
                ('home_adress', models.TextField()),
                ('business_adress', models.TextField()),
                ('car_plate', models.CharField(max_length=35)),
                ('content', models.TextField()),
                ('intelligence_links', models.TextField()),
                ('image1', models.ImageField(blank=True, upload_to='')),
                ('image2', models.ImageField(blank=True, upload_to='')),
                ('image3', models.ImageField(blank=True, upload_to='')),
            ],
        ),
    ]