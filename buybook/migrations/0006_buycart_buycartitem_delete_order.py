# Generated by Django 5.0.6 on 2024-07-26 20:56

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_initial'),
        ('buybook', '0005_alter_buybook_booklang_alter_buybook_booktype'),
        ('sellbook', '0006_alter_category_options_alter_language_options'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BuyCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BuyCartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sellbook.sellbook')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buybook.buycart')),
            ],
        ),
        migrations.DeleteModel(
            name='Order',
        ),
    ]