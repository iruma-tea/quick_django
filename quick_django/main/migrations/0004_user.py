# Generated by Django 5.1.7 on 2025-03-16 04:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('handle', models.CharField(max_length=20, verbose_name='ユーザー名')),
                ('email', models.CharField(max_length=100, verbose_name='メールアドレス')),
                ('author', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.author')),
            ],
        ),
    ]
