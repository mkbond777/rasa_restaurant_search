import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def initialize_app():
    return SendMail()


class SendMail:
    def __init__(self):
        self.message = MIMEMultipart()

    def send_mail(self, receiver_address, cuisine, location):
        # Mail Body
        mail_content = """
                        Hi Manish,\n
                            Below is the list of restaurants in """ + location + " for " + cuisine + " foods." + """
    
                            1. Coffee
                            2. Tea 
                            3. Milk
                        """

        # The mail addresses and password
        sender_address = 'upgrad.rasa.chat@gmail.com'
        sender_pass = 'manish@1992'

        # Setup the MIME
        self.message['From'] = sender_address
        self.message['To'] = receiver_address
        self.message['Subject'] = 'A test mail sent by Python. It has an attachment.'  # The subject line

        # The body and the attachments for the mail
        self.message.attach(MIMEText(mail_content, 'plain'))

        # Create SMTP session for sending the mail
        try:
            session = smtplib.SMTP('smtp.gmail.com', 587)  # use gmail with port
            session.starttls()  # enable security
            session.login(sender_address, sender_pass)  # login with mail_id and password
            text = self.message.as_string()
            session.sendmail(sender_address, receiver_address, text)
            session.quit()
            return "mail sent"
        except Exception as e:
            return str(e)
