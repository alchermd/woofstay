# Generated by Django 4.1.7 on 2023-03-22 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('owners', '0001_initial'),
        ('pets', '0002_pet_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='owners',
            field=models.ManyToManyField(related_name='pets', to='owners.owner'),
        ),
    ]
