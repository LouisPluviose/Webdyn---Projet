# Generated by Django 3.2.13 on 2022-05-16 16:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0003_rename_nom_categorie_nomc'),
    ]

    operations = [
        migrations.AddField(
            model_name='avion',
            name='categorie',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='application.categorie'),
        ),
    ]
