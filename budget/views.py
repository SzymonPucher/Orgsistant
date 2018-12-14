from django.shortcuts import render
import datetime
from django.http import HttpResponse

from .models import Category, Currency, PaymentMethod, Vendor, Location, Product, BoughtProduct, InnerTransfer,\
                    IncomeSource, Income, Loan
from .useful import get_timeframe
"""
Components:
Menu - Side menu, responsive to top one if opened on the phone.
Footer - information about me, some silly statictics.
Pages:
Index page - menu at the top, below that urgent information about loans
             and current states of accounts, options with adding:
             Bought_Product, Income, Inner_transfer or Loan
Categories - list of all categories, with basic statistics, after clicking on category, details are displayed
Vendors - stats by vendor
Accounts - stats of accounts
Localizations - stats for localizations
Products - list of all products with statistics in details(another page)

Summary - summary for chosen timeframe, default: last year. Divided into incomes and spendings

"""


# Create your views here.
def index(request):
    f, l = BoughtProduct.objects.last(), BoughtProduct.objects.first()
    time_frame = get_timeframe(f, l)
    print(time_frame)
    all_bought_today = BoughtProduct.objects.filter(date=datetime.date.today())
    year, month = datetime.date.today().year, datetime.date.today().month
    tms = BoughtProduct.objects.filter(date__year=year, date__month=month)
    total_spend = 0
    for i in tms:
        total_spend += i.price
    print(total_spend)
    cats = []

    all = BoughtProduct.objects.all()
    # for p in all:
    #     if str(p.product.category).split(' -> ')[0] not in cats:
    #         cats.append(str(p.product.category).split(' -> ')[0])
    # print(cats)
    # l_big = []
    # for t in time_frame:
    #     l_inner = []
    #     for c in cats:
    #         l_inner.append(BoughtProduct.objects.filter(date__year=t[1], date__month=t[0], product__category__parent__name=c))
    #     l_big.append(l_inner)
    # print(l_big)
    cat = Category.objects.all()
    ven = Vendor.objects.all()
    locs = Location.objects.all()
    prod = Product.objects.all()
    pm = PaymentMethod.objects.all()
    incsrc = IncomeSource.objects.all()
    inc = Income.objects.all()


    context = {'products': all, 'vendors': ven, 'locs': locs, 'prod': prod, 'pm': pm, 'cat': cat, 'incsrc': incsrc, 'inc': inc, 'spend': total_spend}

    return render(request, 'budget/index.html', context)
