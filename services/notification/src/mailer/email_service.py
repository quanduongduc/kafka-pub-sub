from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import logging
import smtplib
from jinja2 import Environment, FileSystemLoader
from config import *

templates_dir = os.path.abspath(os.path.join(
    os.path.dirname(__file__), 'templates'))
env = Environment(loader=FileSystemLoader(templates_dir))

logger = logging.getLogger(__name__)


def send_account_created_email(to_email, username):
    subject = "Account Created"
    template = env.get_template("account_created_email.html")
    body = template.render(username=username, email=to_email)

    msg = MIMEMultipart()
    msg["From"] = MAIL_DEFAULT_SENDER
    msg["To"] = to_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "html"))
    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USERNAME, SMTP_PASSWORD)
            server.sendmail(MAIL_DEFAULT_SENDER, to_email, msg.as_string())
    except smtplib.SMTPException as e:
        logger.error('SMTP Exception: {}'.format(e))
