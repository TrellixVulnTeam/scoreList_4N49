# Generated by Django 3.0.7 on 2020-06-21 06:19

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_num', models.CharField(max_length=50)),
                ('score', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(10000000), django.core.validators.MinValueValidator(1)], verbose_name='分数')),
            ],
            options={
                'verbose_name': '分数表',
                'verbose_name_plural': '分数表',
            },
        ),
        migrations.CreateModel(
            name='Rank',
            fields=[
                ('c_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='app.Client')),
                ('rank', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)], verbose_name='名次')),
            ],
        ),
    ]
