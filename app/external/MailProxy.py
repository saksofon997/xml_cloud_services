import atexit
import smtplib
import os


class MailProxy:

    def __init__(self):
        self.username = os.environ["MAIL_LOGIN"]
        self.password = os.environ["MAIL_PASSWORD"]

        self._server = smtplib.SMTP('smtp.gmail.com:587')
        self._server.ehlo()
        self._server.starttls()
        self._server.login(self.username, self.password)
        atexit.register(self.quit)

    def _form(self, address, message):
        return "\r\n".join([
            f"From: {self.username}",
            f"To: {address}",
            "Subject: XMLWS Rentals",
            "",
            f"{message}"
        ])

    def send(self, address, message):
        msg = self._form(address, message)
        return self._server.sendmail(self.username, address, msg)

    def quit(self):
        self._server.quit()
