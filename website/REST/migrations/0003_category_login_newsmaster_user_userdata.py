# Generated by Django 3.0.8 on 2020-07-23 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('REST', '0002_news'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category_name', models.CharField(max_length=30)),
                ('Category_description', models.TextField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Login_id', models.IntegerField(max_length=30)),
                ('Login_type', models.CharField(max_length=30)),
                ('status', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='NewsMaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_id', models.IntegerField(max_length=30)),
                ('news_title', models.CharField(max_length=50)),
                ('news_headline', models.CharField(max_length=30)),
                ('news_image', models.ImageField(blank=True, null=True, upload_to='')),
                ('news_assets', models.CharField(max_length=100)),
                ('news_category_id', models.IntegerField(max_length=20)),
                ('news_text', models.CharField(max_length=200, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(max_length=30)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email', models.EmailField(blank=True, max_length=70)),
                ('password', models.CharField(max_length=32)),
                ('mob_no', models.IntegerField(max_length=20)),
                ('OTP', models.IntegerField(max_length=10)),
                ('fb_check', models.CharField(max_length=30)),
                ('loc_latitude', models.FloatField()),
                ('loc_longitude', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(max_length=30)),
                ('news_id', models.IntegerField(max_length=30)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
