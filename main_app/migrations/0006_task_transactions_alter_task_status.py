# Generated by Django 4.0.3 on 2022-04-03 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_alter_task_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='transactions',
            field=models.ManyToManyField(to='main_app.transaction'),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('Yes', 'complete'), ('No', 'incomplete')], max_length=10),
        ),
    ]