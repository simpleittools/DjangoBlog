# Generated by Django 3.1 on 2020-09-02 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0004_auto_20200901_1632'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='snippet',
            field=models.CharField(default='Click Link for more details', max_length=255),
        ),
    ]
