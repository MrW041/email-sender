import smtplib
from email.message import EmailMessage

reciever=input("Enter Reciever Email_Adress")

EMAIL_ADDRESS = 'Your Email_Adress'
EMAIL_PASSWORD = 'Your Email_App_Password'  
TO_EMAIL = reciever


msg = EmailMessage()
msg['Subject'] = 'Your Subject here'
msg['From'] = EMAIL_ADDRESS
msg['To'] = TO_EMAIL


msg.set_content(
    """\

Hello,

        message

Thank You

"""
)




try:
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.send_message(msg)
        print("Email sent successfully.")
except Exception as e:
    print(f"Failed to send email: {e}")