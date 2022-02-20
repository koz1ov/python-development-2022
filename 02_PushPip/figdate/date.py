import datetime
import pyfiglet

def date(fmt="%Y %d %b, %A", font="graceful"):
    date_str = datetime.datetime.now().strftime(fmt)
    return str(pyfiglet.figlet_format(date_str, font))
