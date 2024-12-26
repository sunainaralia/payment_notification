# Generated by Django 5.1.4 on 2024-12-26 06:16

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
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('due_date', models.DateField()),
                ('payment_status', models.CharField(choices=[('Pending', 'Pending'), ('Partial', 'Partial'), ('Paid', 'Paid')], max_length=50)),
                ('amount_due', models.DecimalField(decimal_places=2, max_digits=10)),
                ('notification_sent', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
