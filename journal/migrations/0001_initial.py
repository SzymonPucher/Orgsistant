# Generated by Django 2.1.1 on 2018-10-10 14:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('description', models.TextField(blank=True, max_length=1000)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('attributes', models.TextField(blank=True, max_length=1000)),
                ('content', models.TextField(blank=True, max_length=100000)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='journal.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(unique=True)),
                ('one_sentence_description', models.CharField(max_length=200)),
                ('today_i_learned', models.CharField(blank=True, max_length=200, verbose_name='Today I learned')),
                ('food_eaten', models.CharField(blank=True, max_length=500)),
                ('tags', models.CharField(blank=True, max_length=200)),
                ('content', models.TextField(max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='ElementInList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, max_length=1000)),
            ],
            options={
                'verbose_name_plural': 'List elements',
            },
        ),
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('description', models.TextField(blank=True, max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Month',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(unique=True)),
                ('one_sentence_description', models.CharField(max_length=200)),
                ('tags', models.CharField(max_length=200)),
                ('content', models.TextField(max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='Year',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.PositiveIntegerField(unique=True)),
                ('one_sentence_description', models.CharField(max_length=200)),
                ('tags', models.CharField(max_length=200)),
                ('content', models.TextField(max_length=10000)),
            ],
        ),
        migrations.AddField(
            model_name='elementinlist',
            name='list',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='journal.List'),
        ),
    ]
