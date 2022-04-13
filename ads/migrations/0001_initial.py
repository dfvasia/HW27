# Generated by Django 4.0.4 on 2022-04-13 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('author', models.CharField(max_length=200)),
                ('price', models.PositiveSmallIntegerField()),
                ('description', models.CharField(max_length=1000)),
                ('address', models.CharField(max_length=1000)),
                ('is_published', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Characteristics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
    ]