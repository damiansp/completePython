from abc import ABC, abstractmethod


class Notification(ABC):
    @abstractmethod
    def notify(self, msg, email):
        pass


class Email(Notification):
    def notify(self, msg, email):
        print(f'Emailing "{msg}" to {email}')


class SMS(Notification):
    def notify(self, msg, phone):
        print(f'Texting "{msg}" to {phone}')


class Contact:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone


class NotificationManager:
    def __init__(self, notification, contact):
        self.notification = notification
        self.contact = contact

    def send(self, msg):
        if isinstance(self.notification, Email):
            self.notification.notify(msg, contact.email)
        elif isinstance(self.notification, SMS):
            self.notification.notify(msg, contact.phone)
        else:
            raise Exception('The notification is not supported')


# Better implementation (conform to Liskov Substitution principle)
class Notification(ABC):
    @abstractmethod
    def notify(self, msg):
        pass


class Email(Notification):
    def __init__(self, email):
        self.email = email

    def notify(self, msg):
        print(f'Emailing "{msg}" to {self.email}')


class SMS(Notification):
    def __init__(self, phone):
        self.phone = phone

    def notify(self, msg):
        print(f'Texting "{msg}" to {self.phone}')


class NotificationManager:
    def __init__(self, notification):
        self.notification = notification

    def send(self, msg):
        self.notification.notify(msg)

        
if __name__ == '__main__':
    contact = Contact(
        'John Jacob', 'jj@jingleheimer-schmidt.com', '(213) 456-7890')
    #notification_mgr = NotificationManager(SMS(), contact)
    #notification_mgr.send('Hello, JJ')
    sms_notification = SMS(contact.phone)
    email_notification = Email(contact.email)
    notification_mgr = NotificationManager(sms_notification)
    notification_mgr.send('Hello, John')
    notification_mgr.notification = email_notification
    notification_mgr.send("We're watching you")
