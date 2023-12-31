# Generated by Django 4.2.3 on 2023-08-01 09:55

import django.core.validators
from django.db import migrations, models
import football_lovers.accounts.validators


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_customuser_gender_customuser_profile_picture_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='first_name',
            field=models.CharField(blank=True, max_length=30, null=True, validators=[django.core.validators.MinLengthValidator(2), football_lovers.accounts.validators.only_alphabetical_letters_validator]),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='gender',
            field=models.CharField(blank=True, choices=[('MALE', 'Male'), ('FEMALE', 'Female')], null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='last_name',
            field=models.CharField(blank=True, max_length=30, null=True, validators=[django.core.validators.MinLengthValidator(2), football_lovers.accounts.validators.only_alphabetical_letters_validator]),
        ),
    ]
