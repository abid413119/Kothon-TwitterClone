# Generated by Django 2.1.4 on 2019-01-08 16:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kotha', '0005_auto_20190108_1631'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='kotha',
            options={'ordering': ['-timestamp']},
        ),
    ]