import locale

#Convert to USD Format
def to_usd(value):
        locale.setlocale(locale.LC_ALL, 'en_US.utf-8') 
        s = locale.currency(value, grouping=True)
        return s