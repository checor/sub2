# Generated by Django 2.2.3 on 2019-08-03 17:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Linea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('ubicacion', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Estacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('distancia', models.FloatField(default=0)),
                ('estacion_anterior', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='lineas.Estacion')),
                ('linea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lineas.Linea')),
            ],
        ),
    ]