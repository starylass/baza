# Generated by Django 2.1.15 on 2020-06-09 18:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quality', '0002_auto_20200604_2246'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dimbussinesdev',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='dimclient',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='dimdate',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='dimproduct',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='dimproductfamily',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='dimsalesterritory',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='dimsupplier',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='dimtechnican',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='dimtestprocedure',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='dimtesttools',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='dimtoolprocedure',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='factclaim',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='factclaimcases',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='factsales',
            options={'managed': True},
        ),
    ]