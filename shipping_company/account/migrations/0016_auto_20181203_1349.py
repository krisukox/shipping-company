# Generated by Django 2.1.3 on 2018-12-03 13:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0015_auto_20181203_1317'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='ID_konta',
            new_name='account',
        ),
    ]