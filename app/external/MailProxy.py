import atexit
import smtplib


class MailProxy:

    def __init__(self):
        self.fromaddr = "xmlwsrentals@gmail.com"

        self._server = smtplib.SMTP('smtp.gmail.com:587')
        self._server.ehlo()
        self._server.starttls()
        self._server.login("xmlwsrentals@gmail.com", "amyfozulqzphrdak")
        atexit.register(self.quit)

    def _form(self, address, message):
        return "\r\n".join([
            "From: xmlwsrentals@gmail.com",
            f"To: {address}",
            "Subject: XMLWS Rentals",
            "",
            f"{message}"
        ])

    def send(self, toaddrs, message):
        msg = self._form(toaddrs, message)
        return self._server.sendmail(self.fromaddr, toaddrs, msg)

    def quit(self):
        self._server.quit()
