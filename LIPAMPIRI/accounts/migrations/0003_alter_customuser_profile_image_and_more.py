# Generated by Django 4.2.5 on 2023-09-12 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_userprofile_first_name_userprofile_last_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='profile_image',
            field=models.URLField(default='https://cdn-icons-png.flaticon.com/512/6522/6522516.png'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_picture',
            field=models.URLField(default='https://cdn-icons-png.flaticon.com/512/6522/6522516.png'),
        ),
    ]
