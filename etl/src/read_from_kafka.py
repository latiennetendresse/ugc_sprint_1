from kafka import KafkaConsumer, errors as kafka_errors

from src.core.settings import KafkaSettings
from src.models.views import KafkaMessage
from src.backoff import backoff


class KafkaReader:
    def __init__(self,
                 kafka_config: KafkaSettings):
        self.consumer = None
        self.kafka_config = kafka_config
        self.connect()

    @backoff(error=kafka_errors.NoBrokersAvailable)
    def connect(self):
        self.consumer = KafkaConsumer(
            self.kafka_config.kafka_topic,
            bootstrap_servers=[f'{self.kafka_config.kafka_host}:{self.kafka_config.kafka_port}'],
            auto_offset_reset=self.kafka_config.auto_offset_reset,
            enable_auto_commit=self.kafka_config.enable_auto_commit,
            group_id=self.kafka_config.group_id,
            consumer_timeout_ms=self.kafka_config.consumer_timeout * 1000
        )

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.consumer:
            self.consumer.close()

    def get_data(self) -> list[KafkaMessage]:

        for message in self.consumer:
            user_id = message.key.decode("utf-8").split('_')[0]
            movie_id = message.key.decode("utf-8").split('_')[1]
            viewed_frame = message.value.decode("utf-8")
            yield KafkaMessage(user_id=user_id,
                               film_id=movie_id,
                               viewed_frame=viewed_frame)

    def commit(self):
        self.consumer.commit()
