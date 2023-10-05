# Generated by Django 4.2.5 on 2023-10-05 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_menuitem_url_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menuitem',
            name='url_name',
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='url',
            field=models.URLField(max_length=255, verbose_name='Ссылка'),
        ),
    ]
