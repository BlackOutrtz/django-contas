# Generated by Django 4.2.3 on 2023-07-17 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contas',
            name='valor',
            field=models.CharField(default='SOME STRING', max_length=65),
        ),
    ]
