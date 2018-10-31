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
    timeframe = get_timeframe(f, l)
    print(timeframe)
    all_bought_today = BoughtProduct.objects.filter(date=datetime.date.today())
    context = {'products': all_bought_today}
    return render(request, 'budget/index.html', context)
