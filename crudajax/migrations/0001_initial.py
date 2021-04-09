# Generated by Django 3.1.6 on 2021-02-25 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('eno', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=70)),
                ('email', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=30)),
                ('experience', models.IntegerField()),
            ],
        ),
    ]
