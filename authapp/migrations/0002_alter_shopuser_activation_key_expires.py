# Generated by Django 4.0.3 on 2022-05-13 19:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 15, 19, 36, 19, 208585)),
        ),
    ]
