# Generated by Django 2.2.7 on 2019-11-07 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0002_auto_20191107_2332'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('review', models.CharField(max_length=1000)),
                ('rating', models.IntegerField(default=0)),
            ],
        ),
    ]