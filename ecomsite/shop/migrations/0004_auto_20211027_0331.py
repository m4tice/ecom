# Generated by Django 3.2.8 on 2021-10-27 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_rename_oder_order'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='item',
            new_name='items',
        ),
        migrations.AddField(
            model_name='order',
            name='total',
            field=models.CharField(default='1', max_length=200),
            preserve_default=False,
        ),
    ]
