from functools import lru_cache
from fastapi import Depends
from aiokafka import AIOKafkaProducer

from src.db.kafka_utils import get_kafka_producer


class FilmViewService:
    def __init__(self, kafka: AIOKafkaProducer) -> None:
        self.kafka = kafka

    async def send_timestamp(
        self, user_id: str, film_id: int, timestamp_id: int
    ) -> None:
        await self.kafka.send(
            topic='views',
            key=f'{user_id}_{film_id}'.encode('utf-8'),
            value=f'{timestamp_id}'.encode('utf-8'),
        )


@lru_cache()
def film_view_services(
    kafka: AIOKafkaProducer = Depends(get_kafka_producer),
) -> FilmViewService:
    return FilmViewService(kafka)
