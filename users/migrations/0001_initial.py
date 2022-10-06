# Generated by Django 4.1.1 on 2022-10-06 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('lat', models.DecimalField(decimal_places=10, max_digits=15)),
                ('lng', models.DecimalField(decimal_places=10, max_digits=15)),
            ],
            options={
                'verbose_name': 'Местоположение',
                'verbose_name_plural': 'Местоположения',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=50)),
                ('role', models.CharField(choices=[('Пользователь', 'member'), ('Администратор', 'admin'), ('Модератор', 'moderator')], default='member', max_length=16)),
                ('age', models.PositiveIntegerField(null=True)),
                ('location', models.ManyToManyField(to='users.location')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
    ]
