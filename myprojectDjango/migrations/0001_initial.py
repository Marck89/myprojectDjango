# Generated by Django 3.2.10 on 2022-01-20 09:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskList',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('done', models.BooleanField(default=False)),
                ('description', models.TextField()),
                ('list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myprojectDjango.tasklist')),
            ],
        ),
        migrations.CreateModel(
            name='ListAccess',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=5)),
                ('list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myprojectDjango.tasklist')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
