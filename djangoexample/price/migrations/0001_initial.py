# Generated by Django 5.1.1 on 2024-10-07 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PriceCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pc_value', models.CharField(max_length=20, verbose_name='Цена')),
                ('pc_description', models.CharField(max_length=200, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Цена',
                'verbose_name_plural': 'Цены',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='PriceTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pc_title', models.CharField(max_length=200, verbose_name='Услуга')),
                ('pc_old_price', models.CharField(max_length=200, verbose_name='Старая цена')),
                ('pc_new_price', models.CharField(max_length=200, verbose_name='Новая цена')),
            ],
            options={
                'verbose_name': 'Услуга',
                'verbose_name_plural': 'Услуги',
                'ordering': ['id'],
            },
        ),
    ]
