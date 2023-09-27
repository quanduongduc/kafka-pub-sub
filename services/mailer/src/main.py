from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import config


server = smtplib.SMTP(config.SMTP_SERVER, config.SMTP_PORT)
server.starttls()  # Upgrade the connection to use TLS
server.login(config.SMTP_USERNAME, config.SMTP_PASSWORD)

subject = "Hello, World!"
body = "This is a test email sent from Python."

msg = MIMEMultipart()
msg["From"] = config.MAIL_DEFAULT_SENDER
msg["To"] = "recipient@example.com"
msg["Subject"] = subject

msg.attach(MIMEText(body, "plain"))
server.sendmail(config.MAIL_DEFAULT_SENDER,
                "recipient@example.com", msg.as_string())
server.quit()
