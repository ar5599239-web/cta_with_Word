from dotenv import load_dotenv
import os
import smtplib
from email.message import EmailMessage

print('Starting secure email automation...\n')

# Loads environment variables.
load_dotenv()

# Security measures used guard user information via 'dotenv' tool.pyt 
sender_email = os.getenv('EMAIL_USER')
sender_password = os.getenv('EMAIL_PASS')
recipient_email = os.getenv('EMAIL_RECIP')
smtp_server = os.getenv('EMAIL_HOST')
smtp_port = os.getenv('EMAIL_PORT')

file_path = 'report.docx'

# Create email
msg = EmailMessage()
msg['Subject'] = 'Automated Client Report'
msg['From'] = sender_email
msg['To'] = recipient_email 

msg.set_content('Good afternoon!\n\nPlease find the attached report.\n\n--R,\nAnthony')

# Attach file
try:
    with open(file_path, 'rb') as f:
        msg.add_attachment(
            f.read(),
            maintype='application',
            subtype='vnd.openxmlformats-officedocument.wordprocessingml.document',
            filename=file_path
        )
    print('Attachment added')
except Exception as e:
    print('Attachment Error:', e)
    exit() 

# Send email
try:
    print('Connecting...')

    with smtplib.SMTP_SSL(smtp_server, smtp_port) as smtp:
        smtp.login(sender_email, sender_password)
        smtp.send_message(msg)
        smtp.set_debuglevel(1)

    print('Email sent successfully!')
except Exception as e:
    print('Email Error:', e)
