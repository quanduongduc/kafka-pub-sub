from config import *
from mailer.email_service import send_account_created_email


class TopicHandler:
    def __init__(self, topic) -> None:
        self.topic = topic

    def handle(self, user_data):
        print(user_data)
        if self.topic == USER_CREATING_TOPIC:
            send_account_created_email(
                to_email=user_data['email'], username=user_data['username'])
        else:
            raise Exception(f"Invalid topic {self.topic}")
