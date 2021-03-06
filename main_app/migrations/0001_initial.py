# Generated by Django 4.0.3 on 2022-04-11 06:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Family',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('receiving_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receiving_user', to=settings.AUTH_USER_MODEL)),
                ('sending_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sending_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('duedate', models.DateTimeField()),
                ('description', models.CharField(max_length=200)),
                ('task_status', models.CharField(choices=[('Completed', 'complete'), ('Not yet started', 'not yet started'), ('Incomplete', 'incomplete')], max_length=20)),
                ('task_approval', models.BooleanField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('family', models.ManyToManyField(to='main_app.family')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
