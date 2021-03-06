# Generated by Django 3.1 on 2021-01-21 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tms', '0003_auto_20210121_1228'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeadlineModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deadline_PS2TS', models.DateTimeField(blank=True, null=True)),
                ('deadline_TS2PS', models.DateTimeField(blank=True, null=True)),
                ('is_active_PS2TS', models.BooleanField(default=False)),
                ('is_active_TS2PS', models.BooleanField(default=False)),
                ('message', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
