import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def initialize_app():
    return SendMail()


class SendMail:

    def send_mail(self, recipient, cuisine, loc, restaurants):
        # Mail Body
        res_str = "\n\n".join(restaurants)

        subject = "Your preferred restaurants list"
        body = "Hi,\n\nBelow is the list of top restaurants in " + loc + " for " + cuisine + " foods in your " \
                                                                                             "budget\n\n\n" + res_str

        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)  # connect to smtp server
        server.login("upgrad.rasa.chat@gmail.com", "manish@1992")

        msg = "Subject: {} \n\n {} ".format(subject, body)  # creating the message

        try:
            server.sendmail(  # send the email
                "upgrad.rasa.chat@gmail.com",
                recipient,
                msg.encode('utf-8'))
            server.quit()
            return "Mail Sent"
        except Exception as e:
            return str(e)
