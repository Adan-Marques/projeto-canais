# Generated by Django 5.0 on 2023-12-22 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='analistas',
            fields=[
                ('id_analista', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.TextField(max_length=255)),
                ('email', models.TextField(max_length=255)),
                ('celular', models.TextField(max_length=255)),
                ('canal', models.TextField(max_length=255)),
                ('cargo', models.TextField(max_length=255)),
                ('oferta', models.TextField(max_length=255)),
                ('modulo', models.TextField(max_length=255)),
                ('submodulo', models.TextField(max_length=255)),
            ],
        ),
    ]
