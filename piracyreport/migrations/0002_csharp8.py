# Generated by Django 3.0.2 on 2020-01-16 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('piracyreport', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CSharp8',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=150)),
                ('date_found', models.DateField()),
                ('date_resolved', models.DateField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
