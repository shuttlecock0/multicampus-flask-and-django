import smtplib
from email.message import EmailMessage
from getpass import getpass
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

email_list = ['ssintico88@naver.com', 'qhrtk3218@naver.com']

password = getpass('Password : ')
msg = EmailMessage()
msg['Subject'] = '권고사직서'
msg['From'] = 'shuttlecock0@naver.com'
# msg['To'] = 'ssintico88@naver.com'
# msg.set_content('죄송합니다.')
# s = smplib.SMP_SSL('smtp.naver.com', '465')
# s.login('shuttlecock0', password)
# s.send_message(msg)

msg['To'] = ','.join(email_list)
html = """
<html>
    <body>
    <img src="https://sampleImg.com/asdasd.png">
    <p>HI,</p>
    <a href="https://www.google.com">GO TO GOOGLE</a>
    </body>
</html>
"""

part = MIMEText(html, 'html')
msg.attach(part)
s = smplib.SMP_SSL('smtp.naver.com', '465')
s.login('shuttlecock0', password)
s.send_message(msg)