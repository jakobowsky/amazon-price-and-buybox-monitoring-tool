# Generated by Django 4.1.2 on 2022-10-18 16:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('asin', models.CharField(max_length=250, unique=True)),
                ('is_running', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DataRow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('asin', models.CharField(default='', max_length=250)),
                ('date_of_request', models.DateTimeField(default=django.utils.timezone.now)),
                ('marketplace_id', models.CharField(default='', max_length=250)),
                ('shipping_currency', models.CharField(default='', max_length=250)),
                ('shipping_price', models.FloatField(blank=True, null=True)),
                ('listing_currency', models.CharField(default='', max_length=250)),
                ('listing_price', models.FloatField(blank=True, null=True)),
                ('shipping_max_hours', models.FloatField(blank=True, null=True)),
                ('shipping_min_hours', models.FloatField(blank=True, null=True)),
                ('shipping_availability', models.CharField(default='', max_length=250)),
                ('sub_condition', models.CharField(default='', max_length=250)),
                ('is_featured_merchant', models.BooleanField(default=False)),
                ('is_buy_box_winner', models.BooleanField(default=False)),
                ('is_fulfilled_by_amazon', models.BooleanField(default=False)),
                ('seller_feedback_count', models.IntegerField(blank=True, null=True)),
                ('seller_positive_feedback_rating', models.FloatField(blank=True, null=True)),
                ('response', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
