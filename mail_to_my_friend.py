import smtplib
import sys, getpass
from email.mime.text import MIMEText

print("Python program to send a mail to your friend.")
# fromaddr = "Sender mail id"
# toaddr = "Receiver mail id"
# subject = "Mail from Python program"
fromaddr = input("Enter the sender mail-id: ")
toaddr = input("Enter the receiver(Your friend's) mail-id: ")
subject = input("Enter the Subject for the mail: ")
# body = '''Hello!!!. 

#     This is a mail from python program. I hope you will reply to me after reading this mail.

#  Thanks and Regards.
#  Arun P N'''
print("Press 'Ctrl+Z'-for windows and 'Ctrl+D'-for other OS and 'Enter' key after the end of body of the mail.")
print("Enter the content for the body of the mail.")
msg = sys.stdin.readlines()
body = ""
for x in msg:
    body += x
msg = MIMEText(body)
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = subject
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
# password = "Sender mail Password."
# password = input("Enter your password: ")
password = getpass.getpass(prompt = 'Enter your password: ')
server.login(fromaddr,password)
server.send_message(msg)
print("Mail sent successfully...")
server.quit()
# Note: Before running this program make sure that you have enabled the 'Less secure apps access' of your Gmail account.
# Link for Less secure apps access: https://www.google.com/settings/security/lesssecureapps
