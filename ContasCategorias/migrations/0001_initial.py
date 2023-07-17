# Generated by Django 4.2.3 on 2023-07-17 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agua',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nome_conta', models.CharField(max_length=65)),
                ('vencimento', models.CharField(max_length=65)),
                ('status', models.CharField(default='', max_length=65)),
                ('valor', models.CharField(default='', max_length=65)),
            ],
            options={
                'verbose_name': 'luz',
                'verbose_name_plural': 'Luz',
            },
        ),
        migrations.CreateModel(
            name='Luz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nome_conta', models.CharField(max_length=65)),
                ('vencimento', models.CharField(max_length=65)),
                ('status', models.CharField(default='', max_length=65)),
                ('valor', models.CharField(default='', max_length=65)),
            ],
            options={
                'verbose_name': 'luz',
                'verbose_name_plural': 'Luz',
            },
        ),
        migrations.CreateModel(
            name='Net',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nome_conta', models.CharField(max_length=65)),
                ('vencimento', models.CharField(max_length=65)),
                ('status', models.CharField(default='', max_length=65)),
                ('valor', models.CharField(default='', max_length=65)),
            ],
            options={
                'verbose_name': 'luz',
                'verbose_name_plural': 'Luz',
            },
        ),
        migrations.CreateModel(
            name='PlanoDeSaude',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nome_conta', models.CharField(max_length=65)),
                ('vencimento', models.CharField(max_length=65)),
                ('status', models.CharField(default='', max_length=65)),
                ('valor', models.CharField(default='', max_length=65)),
            ],
            options={
                'verbose_name': 'luz',
                'verbose_name_plural': 'Luz',
            },
        ),
    ]