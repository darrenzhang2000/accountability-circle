# Generated by Django 3.1.5 on 2021-01-31 01:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_auto_20210130_2224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='goals',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='users', to='backend.goals'),
        ),
    ]
