# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-11 16:39
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0002_persona_trabajador'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alquiler',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FechaAlta', models.DateField(null=True)),
                ('FechaIngreso', models.DateField(null=True)),
            ],
            options={
                'verbose_name': 'Alquiler',
                'verbose_name_plural': 'Alquileres',
            },
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('detalle', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ruc', models.CharField(blank=True, max_length=10)),
                ('cliente', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.Persona')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
            },
        ),
        migrations.CreateModel(
            name='DetalleAlquiler',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('boleta', models.CharField(blank=True, max_length=10, null=True)),
                ('factura', models.CharField(blank=True, max_length=10, null=True)),
                ('total', models.FloatField(default=0)),
                ('Trabajador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogo.Cliente')),
            ],
            options={
                'verbose_name': 'DetalleAlquiler',
                'verbose_name_plural': 'DetalleAlquileres',
            },
        ),
        migrations.CreateModel(
            name='Oficina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(blank=True, max_length=10, null=True)),
                ('estado', models.CharField(blank=True, max_length=10, null=True)),
                ('detalle', models.TextField(blank=True, null=True)),
                ('precio', models.CharField(blank=True, max_length=10, null=True)),
                ('dni', models.CharField(blank=True, max_length=10, null=True)),
                ('categoria', models.ManyToManyField(blank=True, null=True, to='catalogo.Categoria', verbose_name='list of Categorias')),
            ],
            options={
                'verbose_name': 'Oficina',
                'verbose_name_plural': 'Oficinas',
            },
        ),
        migrations.AddField(
            model_name='detallealquiler',
            name='oficina',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogo.Oficina'),
        ),
        migrations.AddField(
            model_name='alquiler',
            name='detalleAlquiler',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogo.DetalleAlquiler'),
        ),
    ]