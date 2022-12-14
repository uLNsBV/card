# Generated by Django 4.1 on 2022-08-23 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=250)),
                ('title', models.CharField(max_length=250)),
                ('describtion', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(upload_to='post_images')),
            ],
        ),
    ]
