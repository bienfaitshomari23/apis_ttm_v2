# Generated by Django 3.2.9 on 2022-03-25 05:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20211106_1217'),
        ('dash', '0011_auto_20211126_0307'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='covercity',
            name='company',
        ),
        migrations.AddField(
            model_name='covercity',
            name='company',
            field=models.ForeignKey(
                default=3, on_delete=django.db.models.deletion.CASCADE, related_name='cities', to='account.company'),
            preserve_default=False,
        ),
    ]