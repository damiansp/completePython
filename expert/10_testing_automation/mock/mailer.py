import email.message
import smtplib


def send(sender, to, subject='None', body='None', server='localhost'):
    '''send a msg'''
    msg = email.message.Message()
    msg['To'] = to
    msg['From'] = sender
    msg['Subject'] = subject
    msg.set_payload(body)
    client = smtplib.SMTP(server)
    try:
        return client.sendmail(sender, to, msg.as_string())
    finally:
        client.quit()
        
