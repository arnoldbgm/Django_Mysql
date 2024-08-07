# Generated by Django 5.0.7 on 2024-07-13 22:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=190)),
            ],
        ),
        migrations.CreateModel(
            name='ProductoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=191)),
                ('descripcion', models.TextField()),
                ('precio', models.FloatField()),
                ('categoriaId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='productos', to='tienda.categoriamodel')),
            ],
        ),
    ]
