# Generated by Django 4.2.3 on 2023-07-17 19:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ContasCategorias', '0003_rename_light_luz_alter_agua_options_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Net',
            new_name='Internet',
        ),
        migrations.AlterModelOptions(
            name='internet',
            options={'verbose_name': 'Internet', 'verbose_name_plural': 'Internet'},
        ),
    ]
