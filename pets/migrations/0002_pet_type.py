# Generated by Django 4.1.7 on 2023-03-18 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='type',
            field=models.CharField(choices=[('Dog', 'Dog'), ('Cat', 'Cat')], default='Dog', max_length=255),
            preserve_default=False,
        ),
    ]
