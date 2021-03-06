# Generated by Django 3.2.11 on 2022-04-04 10:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('add', models.URLField(unique=True)),
            ],
            options={
                'verbose_name': 'branch',
                'verbose_name_plural': 'branches',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=250)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stock', models.IntegerField()),
                ('available', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'item',
                'verbose_name_plural': 'items',
                'ordering': ('product',),
            },
        ),
        migrations.CreateModel(
            name='userdetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('ph', models.IntegerField()),
                ('email', models.TextField(unique=True)),
                ('add', models.TextField()),
                ('prod', models.CharField(max_length=250)),
                ('place', models.CharField(max_length=250)),
                ('quantity', models.IntegerField()),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('delivery', models.DateTimeField()),
            ],
            options={
                'db_table': 'Userdetail',
            },
        ),
        migrations.CreateModel(
            name='place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=250)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taskapp.branch')),
            ],
            options={
                'verbose_name': 'place',
                'verbose_name_plural': 'places',
                'ordering': ('pname',),
            },
        ),
    ]
