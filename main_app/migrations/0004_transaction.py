# Generated by Django 4.0.3 on 2022-04-03 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_rename_tasks_task'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_number', models.CharField(max_length=50)),
                ('balance', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateTimeField()),
            ],
        ),
    ]