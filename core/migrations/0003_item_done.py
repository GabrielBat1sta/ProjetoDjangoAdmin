# Generated by Django 4.2.7 on 2023-11-10 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='done',
            field=models.BooleanField(default=False),
        ),
    ]
