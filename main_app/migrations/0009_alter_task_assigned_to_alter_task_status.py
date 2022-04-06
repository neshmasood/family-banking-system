# Generated by Django 4.0.3 on 2022-04-06 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_task_assigned_to_alter_task_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='assigned_to',
            field=models.CharField(choices=[('child', 'child'), ('parent', 'parent')], max_length=20),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('Completed', 'complete'), ('Incomplete', 'incomplete')], max_length=10),
        ),
    ]
