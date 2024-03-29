# Generated by Django 5.0.1 on 2024-01-25 16:48

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40, verbose_name='название товара')),
                ('price', models.IntegerField(verbose_name='цена')),
                ('description', models.CharField(max_length=150, verbose_name='описание товара')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='время создания')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='author_notice', to=settings.AUTH_USER_MODEL, verbose_name='автор')),
            ],
            options={
                'verbose_name': 'объявление',
                'verbose_name_plural': 'объявления',
            },
        ),
    ]
