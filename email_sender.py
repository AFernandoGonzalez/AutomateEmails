# Import smtplib for the actual sending function
import smtplib
# Import the email modules we'll need
from email.message import EmailMessage

from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())

email = EmailMessage()
email['from'] = 'Fer Gon'
email['to'] = 'target_email@gmail.com'
email['subject'] = 'You won a $1,000,000 dollars!'

email.set_content(html.substitute({'name': 'TinTin'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('your_email@gmail.com', 'password')
    smtp.send_message(email)
    print('all good bosss!')


# Other IDEA's
# make this email to be sent at a specific time
