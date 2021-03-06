# Generated by Django 2.2.4 on 2019-08-30 18:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20190830_1536'),
    ]

    operations = [
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.CharField(max_length=11, verbose_name='تلفن همراه')),
                ('desc', models.CharField(blank=True, max_length=200, verbose_name='توضیح')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='تاریخ ثبت')),
            ],
            options={
                'verbose_name': 'اعضا خبرنامه',
                'verbose_name_plural': 'عضو خبرنامه',
            },
        ),
    ]
