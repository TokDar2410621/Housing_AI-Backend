# Generated by Django 5.1.7 on 2025-06-18 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('annonces', '0004_annonce_a_discuter'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='annonce',
            name='a_discuter',
        ),
        migrations.RemoveField(
            model_name='imageannonce',
            name='imageSupplementaireFichier',
        ),
        migrations.RemoveField(
            model_name='imageannonce',
            name='imageSupplementaireUrl',
        ),
        migrations.AlterField(
            model_name='annonce',
            name='prix',
            field=models.CharField(max_length=255),
        ),
    ]
