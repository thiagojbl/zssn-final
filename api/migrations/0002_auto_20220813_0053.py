# Generated by Django 3.2 on 2022-08-13 03:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='negociar',
            old_name='sobrevivente_trocar',
            new_name='sobrevivente1',
        ),
        migrations.RenameField(
            model_name='negociar',
            old_name='sobrevivente_receber',
            new_name='sobrevivente2',
        ),
        migrations.RemoveField(
            model_name='negociar',
            name='status',
        ),
    ]