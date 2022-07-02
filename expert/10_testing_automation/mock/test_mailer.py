import smtplib
from unittest.mock import Mock, patch

from mailer import send


def test_send():
    sender = 'john_d@example.com'
    to = 'jane_d@example.com'
    body = 'Hello, Jane'
    subject = 'Test'
    with patch('smtplib.SMTP') as mock:
        client = mock.return_value
        client.sendmail.return_value = {}
        res = send(sender, to, subject, body)
        assert client.sendmail.called
        assert client.sendmail.call_args[0][0] == sender
        assert client.sendmail.call_args[0][1] == to
        assert subject in client.sendmail.call_args[0][2]
        assert body in client.sendmail.call_args[0][2]
        assert res == {}


def test_send2(monkeypatch):
    sender = 'john_d@example.com'
    to = 'jane_d@example.com'
    body = 'Hello, Jane'
    subject = 'Test'
    smtp = Mock()
    monkeypatch.setattr(smtplib, 'SMTP', smtp)
    client = smtp.return_value
    client.sendmail.return_value = {}
    res = send(sender, to, subject, body)
    assert client.sendmail.called
    assert client.sendmail.call_args[0][0] == sender
    assert client.sendmail.call_args[0][1] == to
    assert subject in client.sendmail.call_args[0][2]
    assert body in client.sendmail.call_args[0][2]
    assert res == {}
