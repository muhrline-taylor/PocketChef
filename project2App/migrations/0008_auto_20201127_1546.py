# Generated by Django 2.2.4 on 2020-11-27 21:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project2App', '0007_restaurant_chefs'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='chefs',
        ),
        migrations.AddField(
            model_name='user',
            name='chefs',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='chefs', to='project2App.Restaurant'),
        ),
    ]
