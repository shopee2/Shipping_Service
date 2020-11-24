from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Carrier)
admin.site.register(OrderItem)
admin.site.register(OrderDescription)