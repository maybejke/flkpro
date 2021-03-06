# Generated by Django 2.2 on 2019-05-14 11:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImageCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='имя')),
                ('description', models.CharField(blank=True, max_length=128, verbose_name='описание')),
                ('is_active', models.BooleanField(default=True, verbose_name='активная категория')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='имя')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Большая картинка')),
                ('mini_image', models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Маленькая картинка')),
                ('short_desc', models.CharField(blank=True, max_length=128, verbose_name='короткое описание')),
                ('description', models.CharField(blank=True, max_length=256, verbose_name='описание')),
                ('is_active', models.BooleanField(default=True, verbose_name='активная картинка')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.ImageCategory')),
            ],
        ),
    ]
