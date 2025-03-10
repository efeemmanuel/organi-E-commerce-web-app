# Generated by Django 4.2.14 on 2025-01-05 12:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('completed', models.BooleanField(default=False)),
                ('discounted_price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50, unique=True)),
                ('discount', models.DecimalField(decimal_places=2, max_digits=5)),
                ('expiration_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('item_photo', models.ImageField(upload_to='products')),
                ('name', models.CharField(max_length=20)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('department', models.CharField(blank=True, choices=[('fruits', 'fruits'), ('vegetables', 'vegetables'), ('meats', 'meats'), ('fast foods', 'fast foods'), ('drinks', 'drinks')], max_length=10)),
                ('producttype', models.CharField(blank=True, choices=[('featured products', 'featured products'), ('latest products', 'latest products'), ('top reated products', 'top reated products'), ('review products', 'review products'), ('sales off', 'sales off')], max_length=30)),
                ('shipping', models.CharField(blank=True, max_length=20)),
                ('avaliabilty', models.CharField(blank=True, max_length=20)),
                ('weight', models.CharField(blank=True, max_length=20)),
                ('description', models.TextField(blank=True, max_length=200)),
                ('information', models.TextField(blank=True, max_length=200)),
                ('reviews', models.TextField(blank=True, max_length=200)),
                ('discount', models.CharField(blank=True, max_length=20)),
                ('old_price', models.CharField(blank=True, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='ShippingDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(default=True, max_length=100)),
                ('lastname', models.CharField(default=True, max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('zip_code', models.CharField(default=True, max_length=50)),
                ('phone_number', models.CharField(default=True, max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('cart', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='appusers.cart')),
                ('shipping_details', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='appusers.shippingdetails')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('cart', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, related_name='cartitems', to='appusers.cart')),
                ('product', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, related_name='items', to='appusers.products')),
            ],
        ),
    ]
