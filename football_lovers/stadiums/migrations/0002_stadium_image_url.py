# Generated by Django 4.2.3 on 2023-07-31 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stadiums', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stadium',
            name='image_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]