# Generated by Django 4.1 on 2022-09-21 09:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mywatchlist', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BarangWishlist',
            new_name='WatchList',
        ),
    ]