# Generated by Django 5.1.4 on 2024-12-19 00:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('First', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Types',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Price', models.IntegerField(null=True)),
                ('P_serial', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='First.create')),
            ],
        ),
    ]
