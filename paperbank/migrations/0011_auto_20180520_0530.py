# Generated by Django 2.0.3 on 2018-05-20 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paperbank', '0010_auto_20180519_1048'),
    ]

    operations = [
        migrations.AddField(
            model_name='bca',
            name='semester',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='biotech',
            name='semester',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='civil',
            name='semester',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='cse',
            name='semester',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='electronics',
            name='semester',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='it',
            name='semester',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='mech',
            name='semester',
            field=models.CharField(max_length=10, null=True),
        ),
    ]