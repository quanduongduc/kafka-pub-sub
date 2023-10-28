import json
import logging
import asyncio
from aiokafka import AIOKafkaConsumer, ConsumerRecord
from mailer.topic_handler import TopicHandler
from consumer import create_consumer
from config import settings

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
    consumer = await create_consumer(topics=[settings.USER_CREATING_TOPIC],
                                     group_id=settings.MAILER_CONSUMER_GROUP)
    await consumer.start()
    await consume_loop(consumer)

asyncio.run(main(), debug=True)
