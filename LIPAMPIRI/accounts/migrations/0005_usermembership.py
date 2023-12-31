# Generated by Django 4.2.5 on 2023-09-12 22:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_customuser_profile_image_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserMembership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('membership_type', models.CharField(blank=True, max_length=30, null=True)),
                ('expiration_date', models.DateField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_trial', models.BooleanField(default=False)),
                ('payment_status', models.CharField(blank=True, choices=[('Paid', 'Paid'), ('Pending', 'Pending'), ('Cancelled', 'Cancelled')], default='Pending', max_length=30, null=True)),
                ('payment_method', models.CharField(blank=True, choices=[('Credit Card', 'Credit Card'), ('PayPal', 'PayPal')], default='Credit Card', max_length=30, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
