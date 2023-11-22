# Generated by Django 4.2.7 on 2023-11-22 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Afisha',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_car', models.CharField(max_length=100)),
                ('created_ad', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Enter your car name')),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='cars/')),
                ('cost', models.PositiveIntegerField()),
                ('type', models.CharField(choices=[('Sedan', 'Sedan'), ('Universal', 'Universal'), ('SUV', 'SUV')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.URLField()),
            ],
        ),
    ]