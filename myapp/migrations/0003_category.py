# Generated by Django 3.2.5 on 2021-07-16 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_like'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='カテゴリー名')),
                ('name_en', models.CharField(max_length=10, verbose_name='カテゴリー名英語')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_ad', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
