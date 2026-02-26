def is_email_valid(m):
    m=str(m)
    if ( "@" in m ) and ( min(m) != "@" ) and ( max(m) != "@"):
        return True
    else:
        return False
        
def is_ihu_email(n):
    n=str(n)
    if (max(n) = "@ihu.gr"):
        return True
    else:
        return False


previous = open('emails.txt','r')
valid= open('ihu_emails.txt','w')
if (is_email_valid(previous)) and (is_ihu_email(previous)):
    valid.write(previous + "\n")
print("Επιτυχημένη Δημιουργία Αρχείου. {write} emails από τα {previous} είναι έγκυρα και ανήκουν στο
ΔΙΠΑΕ!")
    