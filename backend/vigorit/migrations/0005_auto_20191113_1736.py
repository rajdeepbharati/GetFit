# Generated by Django 2.2.7 on 2019-11-13 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vigorit', '0004_auto_20191113_1733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diet',
            name='calories',
            field=models.IntegerField(choices=[(1500, 1500), (2000, 2000), (2500, 2500), (3000, 3000)]),
        ),
    ]
