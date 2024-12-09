# Generated by Django 5.1.4 on 2024-12-09 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CalendarBox',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('message', models.TextField()),
                ('image', models.ImageField(upload_to='advent_images/')),
                ('is_opened', models.BooleanField(default=False)),
            ],
        ),
    ]