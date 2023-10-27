import json
import logging
import asyncio
from aiokafka import AIOKafkaConsumer, ConsumerRecord
from mailer.topic_handler import TopicHandler
from config import KAFKA_BOOTSTRAP_SERVERS, CONSUMER_GROUP, USER_CREATED_TOPIC, USER_CREATING_TOPIC

logging.basicConfig(
    level=logging.ERROR,
    format="%(asctime)s [%(levelname)s] - %(message)s",
)
logger = logging.getLogger(__name__)


async def handle_msg(msg: ConsumerRecord):
    try:
        message_object = json.loads(msg.value)
        topic = msg.topic
        topic_handler = TopicHandler(topic)
        await topic_handler.handle(message_object)
    except json.JSONDecodeError as e:
        logger.error('Error decoding JSON message: {}'.format(e))
    except Exception as ex:
        logger.error('General Exception: {}'.format(ex))


async def consume_loop(consumer: AIOKafkaConsumer):
    try:
        while True:
            msg = await consumer.getone()
            await handle_msg(msg)
    except KeyboardInterrupt:
        pass
    except Exception as ex:
        logger.error('General Exception: {}'.format(ex))
    finally:
        await consumer.stop()


async def main():
    consumer = AIOKafkaConsumer(
        [USER_CREATED_TOPIC, USER_CREATING_TOPIC],
        bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
        group_id=CONSUMER_GROUP,
        enable_auto_commit=False,
        value_deserializer=lambda x: json.loads(x.decode('utf-8')))

    await consumer.start()
    await consume_loop(consumer)

asyncio.run(main())
