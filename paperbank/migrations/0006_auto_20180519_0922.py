# Generated by Django 2.0.3 on 2018-05-19 03:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('paperbank', '0005_strings'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Documents_cse',
            new_name='cse',
        ),
        migrations.RenameField(
            model_name='cse',
            old_name='document_link',
            new_name='cse_link',
        ),
        migrations.RenameField(
            model_name='cse',
            old_name='document_name',
            new_name='cse_name',
        ),
    ]
