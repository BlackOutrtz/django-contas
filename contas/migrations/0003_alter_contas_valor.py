# Generated by Django 4.2.3 on 2023-07-17 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0002_contas_valor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contas',
            name='valor',
            field=models.CharField(default='', max_length=65),
        ),
    ]
