# Generated by Django 3.2.9 on 2022-04-21 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0004_auto_20220419_1248'),
    ]

    operations = [
        migrations.AddField(
            model_name='seletectedjourney',
            name='state',
            field=models.CharField(choices=[('OPTION', 'in option'), ('CORFIMED', 'confirme'), ('CANCELED', 'annule')], default='OPTION', max_length=20, verbose_name='status reservation'),
        ),
    ]
