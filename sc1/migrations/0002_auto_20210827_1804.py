# Generated by Django 3.2.2 on 2021-08-27 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sc1', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobs',
            name='applyby',
        ),
        migrations.RemoveField(
            model_name='jobs',
            name='typeofwork',
        ),
        migrations.AddField(
            model_name='jobs',
            name='details',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='company',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='duration',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='salary',
            field=models.CharField(default='NA', max_length=100),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='startdate',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
