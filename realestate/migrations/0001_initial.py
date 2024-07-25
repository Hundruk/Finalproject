# Generated by Django 5.0.6 on 2024-07-25 12:52

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Estate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('sell', 'Sell'), ('auction', 'Auction')], help_text='For sale or on auction')),
                ('type', models.CharField(choices=[('apartment', 'Apartment'), ('villa', 'Villa'), ('townhouse', 'Townhouse'), ('mansion', 'Mansion'), ('duplex', 'Duplex'), ('castle', 'Castle'), ('other', 'Other')], default='other', help_text='Estate type')),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('description', models.TextField(help_text='Description of the property', null=True)),
                ('rooms', models.PositiveIntegerField(default=1, help_text='Rooms in total')),
                ('bedrooms', models.PositiveIntegerField(default=1)),
                ('bathrooms', models.PositiveIntegerField(default=1)),
                ('size', models.PositiveIntegerField(default=0, help_text='Size of the house in square meters')),
                ('architectural_style', models.CharField(choices=[('contemporary', 'Contemporary'), ('mid-century modern', 'Mid-century Modern'), ('classical revival', 'Classical Revival'), ('tudor', 'Tudor'), ('georgian', 'Georgian'), ('victorian', 'Victorian'), ('gothic revival', 'Gothic Revival'), ('mediterranean', 'Mediterranean'), ('shingle', 'Shingle'), ('italianate', 'Italianate'), ('spanish colonial', 'Spanish Colonial'), ('ranch', 'Ranch'), ('other', 'Other')], default='other', help_text='Style of the house')),
                ('added_date', models.DateTimeField(auto_now_add=True)),
                ('video', models.FileField(blank=True, help_text='optional', upload_to='videos/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('estate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='realestate.estate')),
            ],
        ),
        migrations.CreateModel(
            name='ForSaleEstate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.PositiveIntegerField()),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('estate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='realestate.estate')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='images/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='estate',
            name='images',
            field=models.ManyToManyField(to='realestate.image'),
        ),
        migrations.CreateModel(
            name='OnAuctionEstate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('starting_price', models.PositiveIntegerField()),
                ('asking_price', models.PositiveIntegerField()),
                ('sold_for', models.PositiveIntegerField(blank=True, null=True)),
                ('starting_date', models.DateTimeField(auto_now_add=True)),
                ('end_date', models.DateTimeField()),
                ('estate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='realestate.estate')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Bid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bidding_sum', models.PositiveIntegerField(default=1000)),
                ('bidding_date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('estate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='realestate.onauctionestate')),
            ],
        ),
    ]
