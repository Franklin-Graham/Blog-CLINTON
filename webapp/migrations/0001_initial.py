# Generated by Django 3.2 on 2021-11-27 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Github', models.CharField(max_length=250)),
                ('Facebook', models.CharField(max_length=250)),
                ('Telegram', models.CharField(max_length=250)),
                ('Twitter', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=250)),
                ('Brand_name', models.CharField(max_length=250)),
                ('info', models.TextField()),
                ('About', models.TextField()),
                ('quotes', models.TextField()),
                ('logo_image', models.ImageField(upload_to='pics')),
                ('your_upi', models.CharField(max_length=250)),
                ('contact_1', models.CharField(max_length=250)),
                ('contact_2', models.CharField(max_length=250)),
                ('whatsapp', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resume', models.FileField(upload_to='files')),
            ],
        ),
        migrations.CreateModel(
            name='Github_project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Repository_name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('user_mail', models.EmailField(max_length=200)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Telegram_project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Telegram_bot', models.CharField(max_length=250)),
                ('Telegram_icon', models.ImageField(upload_to='pics')),
            ],
        ),
    ]
