# Generated by Django 2.2 on 2019-05-01 14:32

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0010_auto_20190501_1632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicaldata',
            name='GUID',
            field=models.UUIDField(blank=True, default=uuid.UUID('97d77fea-cac4-4ee7-bbe7-e488fa9e8356'), editable=False, primary_key=True, serialize=False),
        ),
    ]
