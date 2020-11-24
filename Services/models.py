from django.db import models
from django.utils.translation import gettext_lazy as _
import random, string, datetime


# Create your models here.

def serial_generator(size=4, chars=string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def serial_combine():
    serial_1 = "THA"
    serial_2 = serial_generator()
    serial_3 = serial_generator()
    serial_4 = serial_generator()
    return serial_1+serial_2+serial_3+serial_4

class Carrier(models.Model):
    name = models.CharField(_("ชื่อบริษัทขนส่ง"), max_length=50)
    price = models.IntegerField(_("ราคาขนส่ง"))

class OrderItem(models.Model):
    shippingid = models.CharField(_("Tracking Number"), max_length=50, default=serial_combine)
    orderid = models.CharField(_("Order ID"), max_length=50, default="")
    carrier = models.ForeignKey(Carrier, verbose_name=_("บริษัทขนส่ง"), on_delete=models.DO_NOTHING)
    timestamp = models.DateTimeField(_("เวลา"), auto_now=False, auto_now_add=True)
    shop_id = models.CharField(_("Shop ID"), max_length=50, default="")
    sender = models.CharField(_("ชื่อผู้ส่ง"), max_length=50, default="")
    reciever = models.CharField(_("ชื่อผู้รับ"), max_length=50, default="")
    sender_location = models.TextField(_("สถานที่ผู้ส่ง"), default="")
    reciever_location = models.TextField(_("สถานที่ผู้รับ"), default="")

class OrderDescription(models.Model):
    SHIPPING_STATUS_CHOICE = [
        ('O', 'Ordered'),
        ('R', 'Ready'),
        ('S', 'Shipped'),
        ('D', 'Delivered'),
    ]
    status = models.CharField(_("สถานะการจัดส่ง"), max_length=1, choices=SHIPPING_STATUS_CHOICE, default='O')
    orderItem = models.ForeignKey(OrderItem, verbose_name=_("Order Item"), on_delete=models.CASCADE)
    description = models.TextField(_("คำอธิบาย"))
    timestamp = models.DateTimeField(_("เวลา"), auto_now=False, auto_now_add=True)

    def __str__(self):
        return '%s' %(self.orderItem)
