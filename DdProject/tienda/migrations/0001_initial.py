# Generated by Django 3.1.3 on 2022-03-11 16:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaProd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('create', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'categoriaProd',
                'verbose_name_plural': 'categoriasProd',
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='tienda')),
                ('precio', models.FloatField(max_length=60)),
                ('disponibilidad', models.BooleanField(default=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tienda.categoriaprod')),
            ],
            options={
                'verbose_name': 'producto',
                'verbose_name_plural': 'productos',
            },
        ),
    ]
