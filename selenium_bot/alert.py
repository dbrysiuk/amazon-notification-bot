from smtplib import SMTP
from email.message import EmailMessage


class Alert:
    def email_alert(subject, body, to):
        # gmail account
        user = "test.email@gmail.com"
        password = "password"

        # mail message init
        msg = EmailMessage()
        msg.set_content(body)
        msg['subject'] = subject
        msg['to'] = to
        msg['from'] = user

        # mail server init
        server = SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(user, password)

        # send defined message and close mail server connection
        try:
            server.sendmail(user, to, msg.as_string())
        finally:
            print("message was send to " + to + " with content: " + body)
            server.quit()
