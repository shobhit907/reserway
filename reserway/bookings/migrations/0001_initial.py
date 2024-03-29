# Generated by Django 3.1.2 on 2020-11-24 19:46

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0002_bookingagent_credit_card'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoachStructureAC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seatNumber', models.IntegerField()),
                ('seatType', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='CoachStructureSleeper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seatNumber', models.IntegerField()),
                ('seatType', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('age', models.IntegerField(validators=[django.core.validators.MaxValueValidator(200), django.core.validators.MinValueValidator(1)])),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Train',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('train_name', models.CharField(max_length=30)),
                ('dest_station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dest_station', to='bookings.station')),
                ('source_station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='source_station', to='bookings.station')),
            ],
        ),
        migrations.CreateModel(
            name='TrainSchedule',
            fields=[
                ('journey_id', models.AutoField(primary_key=True, serialize=False)),
                ('journey_date', models.DateField()),
                ('num_ac_coaches', models.IntegerField(default=10, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)])),
                ('num_sleeper_coaches', models.IntegerField(default=10, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)])),
                ('train', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookings.train')),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('ticketId', models.AutoField(primary_key=True, serialize=False)),
                ('seat_type', models.CharField(default='AC', max_length=10)),
                ('pnrNumber', models.CharField(max_length=12)),
                ('booking_agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tickets', to='accounts.bookingagent')),
                ('journey', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tickets', to='bookings.trainschedule')),
                ('passenger1', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='ticket1', to='bookings.passenger')),
                ('passenger2', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ticket2', to='bookings.passenger')),
                ('passenger3', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ticket3', to='bookings.passenger')),
                ('passenger4', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ticket4', to='bookings.passenger')),
                ('passenger5', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ticket5', to='bookings.passenger')),
                ('passenger6', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ticket6', to='bookings.passenger')),
            ],
        ),
        migrations.CreateModel(
            name='SleeperBookingStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coachNumber', models.IntegerField()),
                ('seatNumber', models.IntegerField()),
                ('journey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookings.trainschedule')),
                ('passenger', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookings.passenger')),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookings.ticket')),
            ],
        ),
        migrations.CreateModel(
            name='BookingStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('noOfACSeatsRemaining', models.IntegerField()),
                ('noOfSleeperSeatsRemaining', models.IntegerField()),
                ('journey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookings.trainschedule')),
            ],
        ),
        migrations.CreateModel(
            name='ACBookingStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coachNumber', models.IntegerField()),
                ('seatNumber', models.IntegerField()),
                ('journey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookings.trainschedule')),
                ('passenger', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookings.passenger')),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookings.ticket')),
            ],
        ),
    ]
