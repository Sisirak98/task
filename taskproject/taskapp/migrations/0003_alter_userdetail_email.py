# Generated by Django 3.2.12 on 2022-04-09 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskapp', '0002_alter_userdetail_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetail',
            name='email',
            field=models.TextField(),
        ),
    ]
