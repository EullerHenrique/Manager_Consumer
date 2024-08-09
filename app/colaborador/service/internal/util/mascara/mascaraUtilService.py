import re

def mascararEmail(email):
    return email[0] + '*****' + email[email.find('@')-1:] 
    