from django.contrib import admin
from .models import Contact
from .models import Product
from .models import Order
from .models import Snippet

# Register your models here.
admin.site.register(Contact)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Snippet)
