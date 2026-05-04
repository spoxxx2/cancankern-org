import smtplib
from email.message import EmailMessage

# Configuration for Node 1501-P
SENDER_EMAIL = "spoxxx2@gmail.com"
RECEIVER_EMAIL = "spoxxx2@gmail.com" # Sending to yourself as a secure backup
APP_PASSWORD = input("Enter your Google App Password: ")

msg = EmailMessage()
msg['Subject'] = "SECURE BACKUP: PHX-01 Supplemental Disclosure #63/986,721"
msg['From'] = SENDER_EMAIL
msg['To'] = RECEIVER_EMAIL
msg.set_content("Attached: Digital Twin PDF for 1.7kHz Resonant Synthesis (The Fortress). Generated at Node 1501-P, Bakersfield.")

with open("PHX_01_Disclosure.pdf", "rb") as f:
    file_data = f.read()
    msg.add_attachment(file_data, maintype="application", subtype="pdf", filename="PHX_01_Disclosure.pdf")

try:
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(SENDER_EMAIL, APP_PASSWORD)
        smtp.send_message(msg)
    print("Email sent successfully to your vault.")
except Exception as e:
    print(f"Failed to send: {e}")
