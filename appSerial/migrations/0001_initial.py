# Generated by Django 4.2.7 on 2023-12-18 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='dispositivoSistema',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreDispositivo', models.CharField(blank=True, max_length=32, null=True)),
                ('codigoDispositivo', models.CharField(blank=True, max_length=32, null=True)),
                ('fabricanteDispositivo', models.CharField(blank=True, max_length=32, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='usuarioSistema',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreUsuario', models.CharField(blank=True, max_length=32, null=True)),
                ('apellidoUsuario', models.CharField(blank=True, max_length=32, null=True)),
                ('edadUsuario', models.CharField(blank=True, max_length=8, null=True)),
                ('profesionUsuario', models.CharField(blank=True, max_length=64, null=True)),
            ],
        ),
    ]
