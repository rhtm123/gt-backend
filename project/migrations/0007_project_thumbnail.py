# Generated by Django 5.0.6 on 2024-08-08 14:16

import imagekit.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0006_remove_package_price_projectpackageservice_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='thumbnail',
            field=imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to='gt/project/'),
        ),
    ]
