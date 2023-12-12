# Generated by Django 5.0 on 2023-12-12 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LogEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(null=True)),
                ('user', models.CharField(max_length=255, null=True)),
                ('date_time', models.DateTimeField(null=True)),
                ('method', models.CharField(max_length=10, null=True)),
                ('module', models.CharField(max_length=255, null=True)),
                ('table', models.CharField(max_length=255, null=True)),
            ],
        ),
    ]
