import uvicorn
from fastapi import FastAPI
from sse_starlette.sse import EventSourceResponse
from aiokafka import AIOKafkaConsumer
from consumer import get_consumer
from fastapi import Depends

app = FastAPI()


async def consume_message(consumer: AIOKafkaConsumer):
    while True:
        msg = await consumer.getone()
        if msg:
            yield {
                'data': msg.value.decode('utf-8')
            }


@app.get("/")
async def sse_handler(consumer: AIOKafkaConsumer = Depends(get_consumer)):
    return EventSourceResponse(consume_message(consumer))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level='info')
