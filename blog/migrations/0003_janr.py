# Generated by Django 5.0.3 on 2024-06-03 04:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_books'),
    ]

    operations = [
        migrations.CreateModel(
            name='Janr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('janr', models.CharField(max_length=50)),
                ('book', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.books')),
            ],
        ),
    ]
