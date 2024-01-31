# Generated by Django 5.0 on 2024-01-31 16:46

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Canal',
            fields=[
                ('id_canal', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=100)),
                ('cnpj', models.CharField(max_length=20)),
                ('estado', models.CharField(max_length=100)),
                ('regiao', models.CharField(max_length=100)),
                ('tipo', models.CharField(max_length=100)),
                ('contrato', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Oferta',
            fields=[
                ('id_oferta', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=50)),
                ('segmento', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Unidade',
            fields=[
                ('id_unidade', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=100)),
                ('estado', models.CharField(max_length=100)),
                ('tipo', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Analista',
            fields=[
                ('id_analista', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=100)),
                ('sobrenome', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('celular', models.CharField(max_length=100)),
                ('cargo', models.CharField(choices=[('E', 'Estagiário'), ('T', 'Técnico'), ('AI', 'Analista I'), ('AII', 'Analista II'), ('AIII', 'Analista III'), ('C', 'Consultor Especialista'), ('CP', 'Coordenador de Projeto')], max_length=4)),
                ('status', models.CharField(max_length=7)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('canal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_canais.canal')),
            ],
        ),
        migrations.CreateModel(
            name='Modulo',
            fields=[
                ('id_modulo', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=255)),
                ('oferta', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app_canais.oferta')),
            ],
        ),
        migrations.CreateModel(
            name='Submodulo',
            fields=[
                ('id_submodulo', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=255)),
                ('modulo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app_canais.modulo')),
            ],
        ),
        migrations.CreateModel(
            name='AnalistaSubmodulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('analista', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_canais.analista')),
                ('submodulo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_canais.submodulo')),
            ],
        ),
        migrations.AddField(
            model_name='canal',
            name='unidade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app_canais.unidade'),
        ),
    ]
