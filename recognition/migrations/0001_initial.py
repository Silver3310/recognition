# Generated by Django 2.1.3 on 2018-11-02 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(default='no description', max_length=100, verbose_name='Description')),
                ('picture', models.ImageField(blank=True, null=True, upload_to='photos', verbose_name='Picture')),
            ],
            options={
                'verbose_name': 'Request',
                'verbose_name_plural': 'Requests',
            },
        ),
    ]
