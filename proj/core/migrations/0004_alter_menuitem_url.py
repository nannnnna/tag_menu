# Generated by Django 4.2.5 on 2023-10-05 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_remove_menuitem_url_name_alter_menuitem_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='url',
            field=models.CharField(max_length=255, verbose_name='Ссылка'),
        ),
    ]
