# Generated by Django 2.1.1 on 2018-10-17 10:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0004_auto_20181016_2142'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='boughtproduct',
            options={'ordering': ('-date', 'price')},
        ),
        migrations.AlterModelOptions(
            name='currency',
            options={'ordering': ('name',), 'verbose_name_plural': 'Currencies'},
        ),
        migrations.AlterModelOptions(
            name='freeproduct',
            options={'ordering': ('-date', 'product__name')},
        ),
        migrations.AlterModelOptions(
            name='income',
            options={'ordering': ('-date', 'amount')},
        ),
        migrations.AlterModelOptions(
            name='incomesource',
            options={'ordering': ('name',)},
        ),
        migrations.AlterModelOptions(
            name='innertransfer',
            options={'ordering': ('-date', 'source_amount')},
        ),
        migrations.AlterModelOptions(
            name='loan',
            options={'ordering': ('-date', 'amount')},
        ),
        migrations.AlterModelOptions(
            name='location',
            options={'ordering': ('name',)},
        ),
        migrations.AlterModelOptions(
            name='paymentmethod',
            options={'ordering': ('name',)},
        ),
        migrations.AlterModelOptions(
            name='vendor',
            options={'ordering': ('name',)},
        ),
    ]
