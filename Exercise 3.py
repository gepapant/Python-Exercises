def is_leap_year(y):
    return ( y % 4 == 0 and y % 100 != 0 ) or (y % 400 == 0)

def is_valid_date(d,m,yr):
    if d > 0 and d < 31:
        return True
    else:
        return False
    if m > 1 and m < 12:
        return True
    else:
        return False

date = int(input("Καταχώρηση Ημέρας: "))    
month = int(input('Καταχώρηση Μήνα: '))
year = int(input('Καταχώρηση Έτους: '))

if is_valid_date(date, month, year):
    print('Έγκυρη ημερομηνία: {0:2d}/{1:2d}/{2:4d}'.format(date,month,year))
else:
    print("Μη έγκυρη μορφή ημερομηνίας")


        
    