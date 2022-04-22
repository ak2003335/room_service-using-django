# Generated by Django 3.1.6 on 2021-11-13 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0002_auto_20211027_1846'),
    ]

    operations = [
        migrations.CreateModel(
            name='room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_no', models.CharField(max_length=20, null=True, unique=True)),
                ('price', models.CharField(max_length=20, null=True)),
                ('r_type', models.CharField(max_length=20, null=True)),
                ('r_status', models.CharField(max_length=30, null=True)),
                ('r_image', models.FileField(null=True, upload_to='')),
            ],
        ),
    ]