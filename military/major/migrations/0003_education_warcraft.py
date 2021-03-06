# Generated by Django 3.2 on 2021-05-05 13:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0003_auto_20210505_1315'),
        ('major', '0002_delete_education'),
    ]

    operations = [
        migrations.CreateModel(
            name='Warcraft',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('military_area', models.CharField(max_length=20)),
                ('dossier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='warcraft', to='accounts.dossier')),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schoolname', models.CharField(max_length=50)),
                ('dossier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.dossier')),
            ],
        ),
    ]
