# Generated by Django 3.2.9 on 2021-11-24 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0010_alter_placereserved_journey'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seletectedjourney',
            name='session',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='session_journey_selected', to='clients.journeysession', verbose_name='session'),
        ),
    ]
