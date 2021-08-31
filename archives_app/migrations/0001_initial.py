# Generated by Django 3.2.6 on 2021-08-31 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BoxAbbreviations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(blank=True)),
                ('abbreviation', models.CharField(blank=True, max_length=20)),
                ('name', models.CharField(blank=True, max_length=100)),
                ('year', models.IntegerField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='DocumentSubjetc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_subeject', models.CharField(blank=True, max_length=100)),
                ('temporality', models.DateField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='DocumentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_document', models.CharField(blank=True, max_length=100)),
                ('temporality', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='FrontCover',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('box_abbreviation', models.CharField(blank=True, max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='PublicWorker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('cpf', models.CharField(blank=True, max_length=11)),
                ('office', models.CharField(blank=True, max_length=100)),
                ('class_worker', models.CharField(blank=True, max_length=100)),
                ('capacity', models.CharField(blank=True, max_length=100)),
                ('county', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ShelfE',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='ShelfP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filed', models.BooleanField(blank=True)),
                ('unity_that_forwarded', models.CharField(blank=True, max_length=100)),
                ('document_requested', models.CharField(blank=True, max_length=100)),
                ('send_date', models.DateField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Unity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_unity', models.CharField(blank=True, max_length=100)),
                ('unity_abbreviation', models.CharField(blank=True, max_length=20)),
                ('administrative_bond', models.CharField(blank=True, max_length=100)),
                ('bond_abbreviation', models.CharField(blank=True, max_length=20)),
                ('type_of_unity', models.CharField(blank=True, max_length=30)),
                ('municipality', models.CharField(blank=True, max_length=100)),
                ('telephone_number', models.CharField(blank=True, max_length=8)),
                ('note', models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]
