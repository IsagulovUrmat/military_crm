# Generated by Django 3.2 on 2021-05-16 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20210505_1315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
