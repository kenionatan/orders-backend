# Generated by Django 2.1.7 on 2019-03-09 20:38

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grand_total', models.FloatField(default=0)),
                ('create_date', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('update_date', models.DateTimeField(auto_now=True, null=True)),
                ('client', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='orders.Client')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(default=0)),
                ('quantityProduct', models.BigIntegerField(default=1)),
                ('profitability', models.CharField(blank=True, max_length=50, null=True)),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='items', to='orders.Order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Product')),
            ],
        ),
    ]
