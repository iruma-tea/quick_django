# Generated by Django 5.1.7 on 2025-03-15 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_review'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='著者名')),
                ('address', models.CharField(max_length=100, verbose_name='住所')),
                ('books', models.ManyToManyField(to='main.book')),
            ],
        ),
    ]
