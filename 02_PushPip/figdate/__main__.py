import locale
import sys
from .date import date

locale.setlocale(locale.LC_ALL, "ru_RU.UTF-8")
print(date(*sys.argv[1:3]))
