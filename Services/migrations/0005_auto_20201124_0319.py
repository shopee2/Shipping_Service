# Generated by Django 3.1.3 on 2020-11-23 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Services', '0004_orderitem_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='reciever',
            field=models.CharField(default='', max_length=50, verbose_name='ชื่อผู้รับ'),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='reciever_location',
            field=models.TextField(default='', verbose_name='สถานที่ผู้รับ'),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='sender',
            field=models.CharField(default='', max_length=50, verbose_name='ชื่อผู้ส่ง'),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='sender_location',
            field=models.TextField(default='', verbose_name='สถานที่ผู้ส่ง'),
        ),
    ]
