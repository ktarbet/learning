import smtplib
import os

SMTP_USER = os.environ.get("SMTP_USER")
SMTP_SERVER = os.environ.get("SMTP_SERVER")
SMTP_PASS = os.environ.get("SMTP_PASS")

to = SMTP_USER
#to = input("enter email address:")
#message = input("enter message:")
message = "Subject:title\n\n this is email test"
print(SMTP_PASS)

with smtplib.SMTP(SMTP_SERVER) as connection:
    connection.starttls()
    connection.login(user=SMTP_USER, password=SMTP_PASS)
    connection.sendmail(from_addr=SMTP_USER, to_addrs=to, msg=message)
