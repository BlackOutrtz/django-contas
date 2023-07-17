# Generated by Django 4.2.3 on 2023-07-17 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nome_conta', models.CharField(max_length=65)),
                ('data', models.CharField(max_length=65)),
                ('status', models.BooleanField(default=False)),
                ('url', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Conta',
                'verbose_name_plural': 'Contas',
            },
        ),
    ]