# Generated by Django 5.1.7 on 2025-03-29 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(blank=True, max_length=45, null=True)),
                ('name', models.CharField(blank=True, max_length=45, null=True)),
                ('father_name', models.CharField(blank=True, max_length=45, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('number', models.CharField(blank=True, max_length=11, null=True)),
                ('number_polis', models.CharField(blank=True, max_length=16, null=True)),
                ('email', models.EmailField(max_length=45, unique=True)),
                ('password', models.CharField(blank=True, max_length=10, null=True)),
                ('role', models.CharField(default='Пациент', max_length=15)),
            ],
        ),
    ]
