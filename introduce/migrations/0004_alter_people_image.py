# Generated by Django 4.1.7 on 2023-03-14 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('introduce', '0003_alter_people_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='image',
            field=models.ImageField(blank=True, upload_to='image'),
        ),
    ]