# Generated by Django 5.0.3 on 2024-03-29 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_usermodel_is_superuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='is_superuser',
            field=models.BooleanField(default=True),
        ),
    ]