# Generated by Django 4.0.3 on 2022-05-15 12:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0004_alter_shopuser_activation_key_expires_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 17, 12, 25, 7, 570717)),
        ),
    ]
