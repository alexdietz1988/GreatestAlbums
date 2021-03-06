# Generated by Django 4.0.4 on 2022-06-06 13:22

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
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('artist', models.CharField(max_length=250)),
                ('image', models.CharField(default='', max_length=500)),
                ('rank_2003', models.IntegerField(default=0)),
                ('rank_2012', models.IntegerField(default=0)),
                ('rank_2020', models.IntegerField(default=0)),
                ('year', models.IntegerField()),
            ],
            options={
                'ordering': ['rank_2020'],
            },
        ),
        migrations.CreateModel(
            name='MyList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
