# Generated by Django 3.0.6 on 2020-06-25 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PyTraker', '0012_noteboard_note'),
    ]

    operations = [
        migrations.AddField(
            model_name='timers',
            name='totalhours',
            field=models.IntegerField(default=0),
        ),
    ]
