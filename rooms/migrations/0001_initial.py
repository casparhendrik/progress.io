# Generated by Django 3.2.3 on 2021-06-03 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('logo', models.ImageField(default='no_picture.png', upload_to='rooms')),
                ('room', models.CharField(max_length=50)),
                ('progression', models.IntegerField()),
                ('status', models.CharField(max_length=40)),
            ],
        ),
    ]
