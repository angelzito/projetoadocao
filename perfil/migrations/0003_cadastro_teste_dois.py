# Generated by Django 3.1.2 on 2020-10-22 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0002_cadastro_teste'),
    ]

    operations = [
        migrations.AddField(
            model_name='cadastro',
            name='teste_dois',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
