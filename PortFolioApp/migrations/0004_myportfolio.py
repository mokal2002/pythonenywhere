# Generated by Django 5.0.1 on 2024-02-01 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PortFolioApp', '0003_myskills'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyPortfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=1000)),
                ('link', models.URLField(max_length=150)),
                ('image', models.ImageField(default='', upload_to='media/images')),
            ],
        ),
    ]
