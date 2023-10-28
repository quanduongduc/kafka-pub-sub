import logging
from typing import List
from aiokafka import AIOKafkaConsumer
from config import settings


async def create_consumer(topics: List, group_id: str):
    consumer = AIOKafkaConsumer(
        *topics,
        bootstrap_servers=settings.KAFKA_BOOTSTRAP_SERVERS,
        group_id=group_id)
    return consumer


async def get_consumer():
    try:
        consumer = await create_consumer(topics=[settings.USER_CREATED_TOPIC,
                                                 settings.USER_CREATING_TOPIC],
                                         group_id=settings.NOTI_CONSUMER_GROUP)
        await consumer.start()
        yield consumer
    except:
        logging.error('Error while consuming message')
    finally:
        await consumer.stop()
