# Generated by Django 4.1.2 on 2022-11-03 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dcim', '0164_rack_mounting_depth'),
    ]

    operations = [
        migrations.AddField(
            model_name='cable',
            name='comments',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='cable',
            name='description',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='device',
            name='description',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='devicetype',
            name='description',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='module',
            name='description',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='moduletype',
            name='description',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='powerfeed',
            name='description',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='powerpanel',
            name='comments',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='powerpanel',
            name='description',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='rack',
            name='description',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='rackreservation',
            name='comments',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='virtualchassis',
            name='comments',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='virtualchassis',
            name='description',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='virtuallink',
            name='comments',
            field=models.TextField(blank=True),
        ),
    ]
