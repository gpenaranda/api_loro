# Generated by Django 2.1.2 on 2018-10-25 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20181025_2231'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('nombre', models.CharField(blank=True, default='', max_length=100)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]