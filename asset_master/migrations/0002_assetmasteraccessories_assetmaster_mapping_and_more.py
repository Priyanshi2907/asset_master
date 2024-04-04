# Generated by Django 4.2.7 on 2024-03-07 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset_master', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssetMasterAccessories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.CharField(blank=True, max_length=100, null=True)),
                ('fc_no', models.CharField(blank=True, max_length=100, null=True)),
                ('category', models.CharField(blank=True, max_length=100, null=True)),
                ('sub_category', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
                ('brand', models.CharField(blank=True, max_length=100, null=True)),
                ('model_no', models.CharField(blank=True, max_length=100, null=True)),
                ('serial_no', models.CharField(blank=True, max_length=100, null=True)),
                ('sku', models.CharField(blank=True, max_length=100, null=True)),
                ('asset_tag', models.CharField(blank=True, max_length=100, null=True)),
                ('status', models.CharField(blank=True, max_length=100, null=True)),
                ('age', models.CharField(blank=True, max_length=100, null=True)),
                ('box_number', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('last_service_date', models.DateField(blank=True, default=None, null=True)),
                ('upcoming_service_date', models.DateField(blank=True, default=None, null=True)),
                ('length', models.CharField(blank=True, max_length=100, null=True)),
                ('breadth', models.CharField(blank=True, max_length=100, null=True)),
                ('height', models.CharField(blank=True, max_length=100, null=True)),
                ('width', models.CharField(blank=True, max_length=100, null=True)),
                ('warranty_period', models.CharField(blank=True, max_length=100, null=True)),
                ('under_amc', models.BooleanField(default=False)),
                ('amc_date', models.DateField(blank=True, null=True)),
                ('storage_warehouse_number', models.CharField(blank=True, max_length=100, null=True)),
                ('availability', models.BooleanField(default=False)),
                ('outward_date', models.DateField(blank=True, null=True)),
                ('outward_remarks', models.CharField(blank=True, max_length=100, null=True)),
                ('inward_date', models.DateField(blank=True, null=True)),
                ('inward_remarks', models.CharField(blank=True, max_length=100, null=True)),
                ('vendor', models.CharField(blank=True, max_length=100, null=True)),
                ('purchased_on', models.DateField(blank=True, null=True)),
                ('cost_price', models.CharField(blank=True, max_length=100, null=True)),
                ('tax_rate', models.CharField(blank=True, max_length=100, null=True)),
                ('depricated_value', models.CharField(blank=True, max_length=100, null=True)),
                ('created_on', models.DateField(blank=True, null=True)),
                ('rented_asset', models.BooleanField(default=False)),
                ('rental_pricing', models.CharField(blank=True, max_length=100, null=True)),
                ('rent_collected', models.CharField(blank=True, max_length=100, null=True)),
                ('available_for_sale', models.CharField(blank=True, max_length=100, null=True)),
                ('asset_utilization', models.CharField(blank=True, max_length=100, null=True)),
                ('asset_status', models.CharField(blank=True, default='available', max_length=100, null=True)),
                ('repair_type', models.IntegerField(choices=[(10, 'Default Type'), (20, 'External Repair'), (30, 'Internal Repair')], default=10)),
                ('sold_asset', models.BooleanField(default=False)),
                ('loaned_asset', models.BooleanField(default=False)),
                ('loan_period', models.CharField(blank=True, max_length=100, null=True)),
                ('add_to_order', models.BooleanField(default=False)),
                ('confirm_order', models.BooleanField(default=False)),
                ('owner', models.CharField(blank=True, default='Zoom Communication', max_length=100, null=True)),
                ('mapping', models.CharField(blank=True, max_length=100, null=True)),
                ('relation', models.IntegerField(choices=[(101, 'Parent'), (102, 'Child')], default=102)),
                ('image', models.ImageField(blank=True, default=None, null=True, upload_to='media/')),
            ],
        ),
        migrations.AddField(
            model_name='assetmaster',
            name='mapping',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='assetmaster',
            name='relation',
            field=models.IntegerField(choices=[(101, 'Parent'), (102, 'Child')], default=101),
        ),
    ]