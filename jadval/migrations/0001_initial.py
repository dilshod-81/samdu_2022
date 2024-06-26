# Generated by Django 4.2.11 on 2024-05-04 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='PediatryaModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faculty', models.CharField(max_length=200)),
                ('kurs_1', models.CharField(max_length=100)),
                ('kurs_id_1', models.IntegerField(max_length=10)),
                ('kurs_2', models.CharField(max_length=100)),
                ('kurs_id_2', models.IntegerField(max_length=10)),
                ('kurs_3', models.CharField(max_length=100)),
                ('kurs_id_3', models.IntegerField(max_length=10)),
                ('kurs_4', models.CharField(max_length=100)),
                ('kurs_id_4', models.IntegerField(max_length=10)),
                ('kurs_5', models.CharField(max_length=100)),
                ('kurs_id_5', models.IntegerField(max_length=10)),
                ('kurs_6', models.CharField(max_length=100)),
                ('kurs_id_6', models.IntegerField(max_length=10)),
            ],
        ),
    ]
