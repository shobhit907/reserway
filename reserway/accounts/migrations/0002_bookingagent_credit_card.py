# Generated by Django 3.1.2 on 2020-11-19 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookingagent',
            name='credit_card',
            field=models.CharField(default=1, max_length=12),
            preserve_default=False,
        ),
    ]
