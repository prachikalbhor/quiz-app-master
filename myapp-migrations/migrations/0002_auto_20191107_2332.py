# Generated by Django 2.2.7 on 2019-11-07 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='question',
            field=models.CharField(max_length=250),
        ),
    ]
