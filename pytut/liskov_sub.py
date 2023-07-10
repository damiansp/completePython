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

        
if __name__ == '__main__':
    contact = Contact(
        'John Jacob', 'jj@jingleheimer-schmidt.com', '(213) 456-7890')
    notification_mgr = NotificationManager(SMS(), contact)
    notification_mgr.send('Hello, JJ')
