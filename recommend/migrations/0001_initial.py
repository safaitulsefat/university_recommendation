# Generated by Django 5.0.2 on 2024-06-01 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('university', models.CharField(max_length=100)),
                ('rank', models.IntegerField()),
                ('department', models.CharField(choices=[('CSE', 'CSE'), ('EEE', 'EEE')], max_length=3)),
                ('cost', models.IntegerField()),
                ('credit', models.IntegerField()),
                ('weiver', models.BooleanField()),
                ('admission_fee', models.IntegerField()),
                ('minimum_gpa', models.FloatField()),
                ('hostel', models.BooleanField()),
                ('location', models.CharField(max_length=100)),
            ],
        ),
    ]
