# Generated by Django 4.1.7 on 2023-03-15 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('introduce', '0008_alter_people_ability_alter_people_hobby_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='cellphone',
            field=models.CharField(max_length=11, null=True),
        ),
    ]
