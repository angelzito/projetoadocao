# Generated by Django 3.1.2 on 2020-10-22 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cadastro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('denuncia', models.CharField(max_length=100)),
                ('hora', models.CharField(max_length=100)),
                ('local', models.CharField(max_length=100)),
                ('gravidade_alta_ou_muito_alta', models.CharField(max_length=100)),
                ('porte', models.CharField(max_length=100)),
                ('espécie', models.CharField(max_length=100)),
                ('cor', models.CharField(max_length=100)),
                ('contato_do_denunciante', models.CharField(max_length=100)),
            ],
        ),
    ]
