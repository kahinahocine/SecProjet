# Generated by Django 5.1.4 on 2024-12-21 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OtpApp', '0010_alter_otptoken_otp_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otptoken',
            name='otp_code',
            field=models.CharField(default='742cdb', max_length=6),
        ),
    ]
