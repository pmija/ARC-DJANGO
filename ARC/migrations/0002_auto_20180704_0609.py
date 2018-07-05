# Generated by Django 2.0.5 on 2018-07-03 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ARC', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventory',
            name='ItemType',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='inventory',
            name='UniqueID',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='ref_laboratory',
            name='Capacity',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='ref_laboratory',
            name='RoomNum',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='ref_term',
            name='StartDate',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='actualresidency',
            name='ActualResidencyID',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='audittable_inventory',
            name='AuditID',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='group',
            name='GroupID',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='inbox',
            name='InboxID',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='ItemID',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='ref_auditaction',
            name='AuditActionID',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='ref_laboratory',
            name='LabID',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='ref_schedule',
            name='ScheduleID',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='ref_term',
            name='TermID',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='ref_userstatus',
            name='UserStatusID',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='ref_usertype',
            name='UserTypeID',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='residencytimeslot',
            name='ResidencyID',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='studentresidencyschedule',
            name='StudentResSchedID',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='UserID',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]