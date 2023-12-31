# Generated by Django 4.2 on 2023-04-29 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('As_at', models.DateTimeField(auto_now_add=True)),
                ('serial_no', models.CharField(max_length=9, primary_key=True, serialize=False)),
                ('category', models.CharField(max_length=25)),
                ('weight', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('shipping_status', models.CharField(max_length=15)),
            ],
        ),
    ]
