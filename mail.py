import smtplib, ssl
import os
from dotenv import load_dotenv
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from content import content
from pathlib import Path
load_dotenv()
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Variables >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#
sender_email = os.environ["SENDER"]
Theme = "Autonomous Navigation and Robotics"
password = os.environ["PASSWORD"]
# receiver_email = "nskknk17@gmail.com"
FILEPATH = "./docs/"


def formatMail(receiver_email):
    message = MIMEMultipart("alternative")
    message["Subject"] = f"Application for Remote Internship Opportunity in {Theme}(January - May 2024)"
    message["From"] = "Vardan Mittal"
    message["To"] = receiver_email
    part1 = MIMEText(content("text","Vardan Mittal", "Tal"), "plain")
    part2 = MIMEText(content("html","Vardan Mittal", "Tal"), "html")

    message.attach(part1)
    message.attach(part2)

def mailSender(receiver_email,message):
    ############################## Adding Attatchments ##############################

    files = [f"{FILEPATH}resume.pdf", f"{FILEPATH}cover_letter.pdf"]

    for path in files:
        part = MIMEBase("application", "octet-stream")
        with open(path,'rb') as file:
            part.set_paaddiyload(file.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition',
                            'attachment; filename={}'.format(Path(path).name))
        message.attach(part)
    ##<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Send Mail >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>##
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        print("Sending mail....")
        server.login(sender_email, password)
        server.sendmail(sender_email,receiver_email,message.as_string())
    print("Mail Sent!!🎉")
