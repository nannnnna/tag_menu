# Generated by Django 4.2.5 on 2023-10-04 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='url_name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Имя URL'),
        ),
    ]
