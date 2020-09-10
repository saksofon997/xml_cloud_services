import pytest


from app.test.utils.Environment import environ


def test_send(mocker):
    mocker.patch("os.environ", value=environ)
    smtp_constructor_mock = mocker.patch('smtplib.SMTP')
    smtp_mock = smtp_constructor_mock.return_value

    from app.external.MailProxy import MailProxy

    smtp_client = MailProxy()

    result = smtp_client.send("address", "subject", "message")

    assert smtp_mock.login.called
    assert result is True
