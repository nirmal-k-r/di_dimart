# Generated by Django 4.2.5 on 2025-02-13 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('userId', models.IntegerField()),
                ('productId', models.IntegerField()),
            ],
        ),
    ]
