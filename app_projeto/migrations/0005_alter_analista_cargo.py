# Generated by Django 5.0 on 2024-01-05 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_projeto', '0004_alter_analista_email_alter_analista_oferta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='analista',
            name='cargo',
            field=models.TextField(choices=[('F', 'Feminino'), ('M', 'Masculino'), ('N', 'Nenhuma das opções')], max_length=1),
        ),
    ]
