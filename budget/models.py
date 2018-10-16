from django.db import models
# Create your models here.


class Currency(models.Model):
    name = models.CharField(max_length=3, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Currencies"


class PaymentMethod(models.Model):
    name = models.CharField(max_length=32, unique=True)
    currency = models.ForeignKey(Currency, on_delete=models.PROTECT, default=1)
    description = models.TextField(max_length=100, blank=True)

    def __str__(self):
        return self.name


class Vendor(models.Model):
    name = models.CharField(max_length=32, unique=True)
    description = models.TextField(max_length=100, blank=True)

    def __str__(self):
        return self.name


class Location(models.Model):
    name = models.CharField(max_length=32, unique=True)
    description = models.TextField(max_length=100, blank=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    parent = models.ForeignKey('self',blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    name = models.CharField(max_length=32)
    budget = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True)
    description = models.TextField(max_length=200, blank=True)

    def __str__(self):
        full_path = [self.name]
        k = self.parent
        while k is not None:
            full_path.append(k.name)
            k = k.parent
        return ' -> '.join(full_path[::-1])

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ('parent__parent__name','parent__name','name')

    def cat(self, name):
        cats = []
        while self.parent:
            cats.append(self.name)
            self = self.parent
        if name in cats:
            return True
        return False


class Product(models.Model):
    name = models.CharField(max_length=64)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    description = models.TextField(max_length=300, blank=True)

    def __str__(self):
        return self.name + ' - ' + str(self.category)

    def is_food(self):
        if 'Food' in str(self.category):
            return True
        return False


class BoughtProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    currency = models.ForeignKey(Currency, on_delete=models.PROTECT, default=1)
    payment_method = models.ForeignKey(PaymentMethod, on_delete=models.PROTECT, default=1)
    date = models.DateField()
    vendor = models.ForeignKey(Vendor, on_delete=models.PROTECT, default=1)
    location = models.ForeignKey(Location, on_delete=models.PROTECT, default=1)

    def __str__(self):
        return str(self.price) + str(self.currency) + ' ' + str(self.product)


class FreeProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    date = models.DateField()
    estimated_value = models.DecimalField(max_digits=9, decimal_places=2)
    source = models.CharField(max_length=32, blank=True)
    location = models.ForeignKey(Location, on_delete=models.PROTECT, default=1)
    description = models.TextField(max_length=50, blank=True)

    def __str__(self):
        return str(self.product)


class InnerTransfer(models.Model):
    source = models.ForeignKey(PaymentMethod, on_delete=models.PROTECT, related_name='Transfer_from')
    destination = models.ForeignKey(PaymentMethod, on_delete=models.PROTECT, related_name='Transfer_to')
    source_amount = models.DecimalField(max_digits=9, decimal_places=2)
    source_currency = models.ForeignKey(Currency, on_delete=models.PROTECT, default=1, related_name='Source_currency')
    destination_amount = models.DecimalField(max_digits=9, decimal_places=2)
    destination_currency = models.ForeignKey(Currency, on_delete=models.PROTECT, default=1, related_name='Destination_currency')
    date = models.DateField()
    description = models.TextField(max_length=50, blank=True)

    def __str__(self):
        return str(self.source_amount) + ' ' + str(self.source_currency) + ' | ' + str(self.source) + ' -> ' + str(self.destination)


class IncomeSource(models.Model):
    name = models.CharField(max_length=32, unique=True)
    description = models.TextField(max_length=100, blank=True)

    def __str__(self):
        return self.name


class Income(models.Model):
    source = models.ForeignKey(IncomeSource, on_delete=models.PROTECT)
    destination = models.ForeignKey(PaymentMethod, on_delete=models.PROTECT)
    amount = models.DecimalField(max_digits=9, decimal_places=2)
    currency = models.ForeignKey(Currency, on_delete=models.PROTECT, default=1)
    date = models.DateField()
    description = models.CharField(max_length=32, blank=True)

    def __str__(self):
        return str(self.source) + ' | ' + str(self.amount) + ' ' + str(self.currency)


class Loan(models.Model):
    lender = models.CharField(max_length=32)
    borrower = models.CharField(max_length=32)
    amount = models.DecimalField(max_digits=9, decimal_places=2)
    currency = models.ForeignKey(Currency, on_delete=models.PROTECT, default=1)
    account = models.ForeignKey(PaymentMethod, on_delete=models.PROTECT)
    date = models.DateField(null=True, blank=True)
    due = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=32, choices=(('Active', 'Active'),('Overtime', 'Overtime'),('Paid off', 'Paid off')))
    description = models.TextField(max_length=1000, blank=True)

    def __str__(self):
        return str(self.amount) + ' ' + str(self.currency) + ' | ' + self.lender + ' -> ' + self.borrower
