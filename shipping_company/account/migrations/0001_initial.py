# Generated by Django 2.1.3 on 2018-11-28 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('ID_konta', models.AutoField(primary_key=True, serialize=False)),
                ('PESEL', models.IntegerField()),
            ],
        ),
    ]