# Generated by Django 2.1.1 on 2018-10-10 17:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('budget', '0001_initial'),
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
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('image', models.ImageField(upload_to='')),
                ('cooking_time', models.DurationField()),
                ('estimated_price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('ingredients', models.TextField(max_length=2000)),
                ('cooking_instructions', models.TextField(max_length=10000)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='nutrition.Category')),
                ('currency', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='budget.Currency')),
            ],
        ),
    ]
