# Generated by Django 2.1.4 on 2019-01-05 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kotha',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('content1', models.TextField()),
                ('content2', models.TextField()),
            ],
        ),
    ]
