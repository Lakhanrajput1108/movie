# Generated by Django 2.2.6 on 2019-10-14 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0002_auto_20191010_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movieinfo',
            name='mdate',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
