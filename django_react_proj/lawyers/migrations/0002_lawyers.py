# Generated by Django 4.1.7 on 2023-03-31 01:15

from django.db import migrations

def create_data(apps, schema_editor):
    Lawyer = apps.get_model('lawyers', 'Lawyer')
    Lawyer(name="Matt Money", email="mat@gmail.com", document="PE Law", phone="7342490075").save()

class Migration(migrations.Migration):

    dependencies = [
        ('lawyers', '0001_initial'),
    ]

    # perform when migration is triggered
    operations = [
        migrations.RunPython(create_data),
    ]
