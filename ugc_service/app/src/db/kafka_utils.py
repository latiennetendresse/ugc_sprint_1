from aiokafka import AIOKafkaProducer

from src.settings import settings


class KafkaContainer:
    def __init__(self):
        self._producer = None

    async def start(self):
        if not self._producer:
            self._producer = AIOKafkaProducer(
                bootstrap_servers=f'{settings.kafka_host}:{settings.kafka_port}'
            )
            await self._producer.start()

    async def stop(self):
        if self._producer:
            await self._producer.stop()
            self._producer = None

    @property
    def producer(self):
        return self._producer


kafka_container = KafkaContainer()


def get_kafka_producer() -> AIOKafkaProducer:
    return kafka_container.producer
