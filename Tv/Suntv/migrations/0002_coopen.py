# Generated by Django 5.1.4 on 2024-12-21 00:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Suntv', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coopen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=45)),
                ('Age', models.IntegerField(null=True)),
                ('Number', models.IntegerField(null=True)),
                ('P_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Suntv.fund')),
            ],
        ),
    ]
