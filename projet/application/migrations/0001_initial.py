# Generated by Django 3.2.13 on 2022-04-12 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Avion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('date_production', models.DateField(blank=True, null=True)),
                ('nombre_appareils', models.IntegerField()),
                ('presentation', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
