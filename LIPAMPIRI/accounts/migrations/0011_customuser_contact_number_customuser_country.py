# Generated by Django 4.2.5 on 2023-11-21 03:38

from django.db import migrations
import django_countries.fields
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_customuser_date_of_birth_customuser_signup_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='contact_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, help_text='011 123 4567', max_length=128, null=True, region=None),
        ),
        migrations.AddField(
            model_name='customuser',
            name='country',
            field=django_countries.fields.CountryField(default='ZA', max_length=2),
        ),
    ]