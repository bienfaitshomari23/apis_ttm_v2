# Generated by Django 3.2.9 on 2022-10-16 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dash', '0011_alter_journeytarif_devise'),
    ]

    operations = [
        migrations.AddField(
            model_name='routing',
            name='level',
            field=models.IntegerField(default=0, help_text='level of deeper of route'),
        ),
    ]