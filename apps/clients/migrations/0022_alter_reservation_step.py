# Generated by Django 3.2.9 on 2022-11-26 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0021_auto_20221126_2028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='step',
            field=models.IntegerField(choices=[(1, 'SELECT_JOURNEY'), (2, 'PASSENGER'), (3, 'OTHER_INFO'), (4, 'COMPLETED')], default=1, verbose_name='step reservation'),
        ),
    ]