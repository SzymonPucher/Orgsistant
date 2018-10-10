# Generated by Django 2.1.1 on 2018-10-10 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizer', '0002_auto_20181010_1516'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=64, unique=True),
        ),
    ]
