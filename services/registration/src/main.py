from fastapi import FastAPI
from fastapi import Depends
from src.schema import UserRegistration
from src.config import settings
from src.dependencies import get_producer
from aiokafka import AIOKafkaProducer
from worker.main import create_task

app = FastAPI()


@app.post("/")
async def register_user(
    user_data: UserRegistration,
    kafka_producer: AIOKafkaProducer = Depends(get_producer),
):
    await kafka_producer.send(settings.USER_CREATING_TOPIC,
                              user_data.model_dump_json().encode('utf-8'))
    message = create_task.delay("Hello new user")
    return {"message": f"User registered successfully", "user_data": user_data}
