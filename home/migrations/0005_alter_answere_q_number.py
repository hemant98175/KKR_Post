# Generated by Django 4.1.2 on 2022-11-26 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_answere'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answere',
            name='q_number',
            field=models.IntegerField(),
        ),
    ]
