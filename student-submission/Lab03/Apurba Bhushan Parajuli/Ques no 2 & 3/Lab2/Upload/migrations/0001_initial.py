# Generated by Django 4.2.1 on 2023-07-13 13:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Cat', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Files',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uploads', models.ImageField(blank=True, upload_to='my_picture')),
                ('Files', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cat.tasks')),
            ],
        ),
    ]
