# Generated by Django 2.2.2 on 2019-07-08 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='address',
            field=models.CharField(blank=True, default='my address', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='email',
            field=models.CharField(blank=True, default='name@domain.com', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='phone',
            field=models.CharField(blank=True, default='+970590000000', max_length=255, null=True),
        ),
    ]
