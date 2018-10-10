from django.contrib import admin

# Register your models here.
from .models import Category, Currency, PaymentMethod, Vendor, Location, Product, BoughtProduct, InnerTransfer,\
                    IncomeSource, Income, Loan

admin.site.register(Category)
admin.site.register(Currency)
admin.site.register(Vendor)
admin.site.register(PaymentMethod)
admin.site.register(Location)
admin.site.register(Product)
admin.site.register(BoughtProduct)
admin.site.register(InnerTransfer)
admin.site.register(IncomeSource)
admin.site.register(Income)
admin.site.register(Loan)
