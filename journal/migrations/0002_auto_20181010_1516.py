# Generated by Django 2.1.1 on 2018-10-10 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='id',
        ),
        migrations.RemoveField(
            model_name='day',
            name='id',
        ),
        migrations.RemoveField(
            model_name='list',
            name='id',
        ),
        migrations.RemoveField(
            model_name='month',
            name='id',
        ),
        migrations.RemoveField(
            model_name='year',
            name='id',
        ),
        migrations.AddField(
            model_name='day',
            name='food_eaten',
            field=models.TextField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=30, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='day',
            name='date',
            field=models.DateField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='day',
            name='tags',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='day',
            name='today_i_learned',
            field=models.CharField(blank=True, max_length=200, verbose_name='Today I learned'),
        ),
        migrations.AlterField(
            model_name='list',
            name='name',
            field=models.CharField(max_length=30, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='month',
            name='date',
            field=models.DateField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='year',
            name='year',
            field=models.PositiveIntegerField(primary_key=True, serialize=False),
        ),
    ]
