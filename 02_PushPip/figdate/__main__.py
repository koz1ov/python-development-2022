import locale
import sys
from .date import date

locale.setlocale(locale.LC_ALL, "ru_RU.UTF-8")
argc = len(sys.argv)
if argc <= 1:
    print(date()) 
elif argc == 2:
    print(date(sys.argv[1]))
else:
    print(date(sys.argv[1], sys.argv[2]))
