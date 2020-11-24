# Generated by Django 3.1.2 on 2020-11-24 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('f_search', '0003_auto_20201124_1703'),
    ]

    operations = [
        migrations.RenameField(
            model_name='routes',
            old_name='journey_id',
            new_name='journey',
        ),
        migrations.RemoveField(
            model_name='journey',
            name='id',
        ),
        migrations.AddField(
            model_name='journey',
            name='train_id',
            field=models.IntegerField(default=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='journey',
            name='train_name',
            field=models.CharField(default='asdf', max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='journey',
            name='j_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
