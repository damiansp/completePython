import smtplib
from urllib.request import urlopen


URL = 'https://docs.python.org/3/tutorial/stdlib.html'
with urlopen(URL) as resp:
    for line in resp:
        line = line.decode('utf-8') # binary -> text
        if 'python' in line.lower():
            print(line)


# requires a mailserver running on localhost
server = smtplib.SMTP('localhost')
to = 'damiansp@gmail.com'
frm = 'dsatterthwaite@cbtnuggets.com'
body = (
f'''To: {to}
From: {frm}

Beware the Ides of March.''')
server.sendmail(frm, to, body)
server.quit()
