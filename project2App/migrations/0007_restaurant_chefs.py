# Generated by Django 2.2.4 on 2020-11-27 21:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project2App', '0006_auto_20201127_1410'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='chefs',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='chefs', to='project2App.User'),
        ),
    ]
