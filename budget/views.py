from django.shortcuts import render
import datetime
from django.http import HttpResponse

from .models import Category, Currency, PaymentMethod, Vendor, Location, Product, BoughtProduct, InnerTransfer, \
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
    # f, l = BoughtProduct.objects.last(), BoughtProduct.objects.first()
    # time_frame = get_timeframe(f, l)
    # print(time_frame)

    year, month = datetime.date.today().year, datetime.date.today().month

    ms = []
    ts = 0
    for i in range(12):
        total_spend = 0
        total_inc = 0
        if month - i < 1:
            y = year - 1
            m = month - i + 12
            x = BoughtProduct.objects.filter(date__year=y, date__month=m)
            inc = Income.objects.filter(date__year=y, date__month=m)
        else:
            y = year
            m = month - i
            x = BoughtProduct.objects.filter(date__year=y, date__month=m)
            inc = Income.objects.filter(date__year=y, date__month=m)
        for p in x:
            total_spend += p.price
        for p in inc:
            total_inc += p.amount
        ts += total_inc - total_spend
        ms.append([total_spend, m, y, total_inc, total_inc-total_spend])

    context = {'products': BoughtProduct.objects.filter(date=datetime.date.today()), 'spend': ms[::-1], 'ts': ts}

    return render(request, 'budget/index.html', context)
