# Generated by Django 2.2.4 on 2020-11-29 23:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project2App', '0010_auto_20201129_1622'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='restaurant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='restaurantPictures', to='project2App.Restaurant'),
        ),
        migrations.AlterField(
            model_name='image',
            name='uploader',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='userPictures', to='project2App.User'),
        ),
        migrations.AlterField(
            model_name='user',
            name='chefs',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='chefs', to='project2App.Restaurant'),
        ),
    ]
