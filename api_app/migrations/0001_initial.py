# Generated by Django 3.2.12 on 2022-02-28 21:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manufacturer', models.CharField(max_length=50)),
                ('model_name', models.CharField(max_length=50)),
                ('year_production', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manufacture_id', models.TextField()),
                ('manufacturing_date', models.DateField()),
                ('car_model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_app.carmodel')),
            ],
        ),
    ]
