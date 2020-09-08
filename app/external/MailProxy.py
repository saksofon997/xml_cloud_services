import atexit
import smtplib
import os
import logging


class MailProxy:

    def __init__(self):
        self.username = os.environ["MAIL_LOGIN"]
        self.password = os.environ["MAIL_PASSWORD"]
        self.smtp = os.environ["GMAIL_SMTP"]

        self._server = smtplib.SMTP(self.smtp)
        self._server.ehlo()
        self._server.starttls()
        self._server.login(self.username, self.password)

        atexit.register(self.quit)

    def _form(self, address: str, subject: str, message: str):
        return os.linesep.join([
            f"From: {self.username}",
            f"To: {address}",
            f"Subject: {subject}",
            "",
            f"{message}"
        ])

    def send(self, address: str, subject: str, message: str) -> bool:
        try:
            msg = self._form(address, subject, message)
            self._server.sendmail(self.username, address, msg)

            return True
        except Exception as e:
            logging.error(f"Sending Email failed due to {e}.")

    def quit(self):
        self._server.quit()
