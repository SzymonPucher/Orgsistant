import datetime
from .models import *
import organizer.models

def get_timeframe(f, l):
    timeframe = []
    f_months = range(f.date.month, 13)
    l_months = range(1, l.date.month + 1)
    if f.date.year == l.date.year:
        for m in range(f.date.month, l.date.month + 1):
            timeframe.append([m, f.date.year])
        return timeframe
    for m in f_months:
        timeframe.append([m, f.date.year])

    for y in range(f.date.year + 1, l.date.year):
        for m in range(f.date.month + 1, l.date.month):
            timeframe.append([m, y])

    for m in l_months:
        timeframe.append([m, l.date.year])
    return timeframe



def load_data():
    import pandas as pd
    # load location
    Currency(name='PLN').save()
    Currency(name='EUR').save()
    df = pd.read_csv('C:/Users/Szymon/Documents/OrgBackup/loc.txt', sep='\t', header=None)
    for index, row in df.iterrows():
        Location(name=row[0]).save()

    df = pd.read_csv('C:/Users/Szymon/Documents/OrgBackup/ven.txt', sep='\t', header=None)
    for index, row in df.iterrows():
        Vendor(name=row[0]).save()

    df = pd.read_csv('C:/Users/Szymon/Documents/OrgBackup/pm.txt', sep='\t', header=None)
    for index, row in df.iterrows():
        PaymentMethod(name=row[0], currency=Currency.objects.get(name='PLN')).save()

    df = pd.read_csv('C:/Users/Szymon/Documents/OrgBackup/incsrc.txt', sep='\t', header=None)
    for index, row in df.iterrows():
        IncomeSource(name=row[0]).save()

    df = pd.read_csv('C:/Users/Szymon/Documents/OrgBackup/precat.txt', sep='\t', header=None)
    for index, row in df.iterrows():
        Category(name=row[0]).save()

    df = pd.read_csv('C:/Users/Szymon/Documents/OrgBackup/cat.txt', sep='\t', header=None)
    for index, row in df.iterrows():
        Category(name=row[0], parent=Category.objects.get(name=row[1])).save()

    df = pd.read_csv('C:/Users/Szymon/Documents/OrgBackup/p.txt', sep='\t', header=None)
    for index, row in df.iterrows():
        Product(name=row[0], category=Category.objects.get(name=row[1].split(' -> ')[-1])).save()

    df = pd.read_csv('C:/Users/Szymon/Documents/OrgBackup/bp.txt', sep='\t', header=None)
    for index, row in df.iterrows():
        BoughtProduct(product=Product.objects.get(name=row[0], category__name=row[1]),
                      price=row[3],
                      currency=Currency.objects.get(name='PLN'),
                      payment_method=PaymentMethod.objects.get(name=row[4]),
                      date=row[5],
                      vendor=Vendor.objects.get(name=row[6]),
                      location=Location.objects.get(name=row[7])).save()

    df = pd.read_csv('C:/Users/Szymon/Documents/OrgBackup/inc.txt', sep='\t', header=None)
    for index, row in df.iterrows():
        Income(source=IncomeSource.objects.get(name=row[0]),
               destination=PaymentMethod.objects.get(name=row[1]),
               amount=row[2],
               currency=Currency.objects.get(name='PLN'),
               date=row[3]).save()

    df = pd.read_csv('C:/Users/Szymon/Documents/OrgBackup/pomoses.txt', sep='\t', header=None)
    cats = []
    import datetime
    for cat in df.iloc[:, 0].values:
        if cat not in cats:
            organizer.models.Category(name=cat).save()
            cats.append(cat)
    for index, row in df.iterrows():
        organizer.models.PomodoroSession(category=organizer.models.Category.objects.get(name=row[0]), date=row[1], duration=datetime.timedelta(minutes=25)).save()
