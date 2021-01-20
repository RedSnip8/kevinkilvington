# Generated by Django 3.1.5 on 2021-01-20 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20210120_2239'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='client_name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='picture',
            name='photo_description',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='picture',
            name='photo_name',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
