from pydantic import Field
from pydantic_settings import BaseSettings


class KafkaSettings(BaseSettings):
    kafka_host: str = Field('localhost', env='KAFKA_HOST')
    kafka_port: int = Field('9092', env='KAFKA_HOST')
    kafka_topic: str = Field('views', env='KAFKA_TOPIC')
    batch_size: int = Field(1, env='BATCH_SIZE')
    consumer_timeout: int = Field(1, env='CONSUMER_TIMEOUT')
    auto_offset_reset: str = 'earliest'
    group_id: str = 'echo-messages-to-stdout'
    enable_auto_commit: bool = False

    class Config:
        extra = "ignore"
        env_file = 'src/.env'
        env_file_encoding = 'utf-8'


class ClickHouseSettings(BaseSettings):
    clickhouse_host: str = Field('clickhouse-node1', env='CLICKHOUSE_HOST')

    class Config:
        extra = "ignore"
        env_file = 'src/.env'
        env_file_encoding = 'utf-8'


kafka_config = KafkaSettings()
clickhouse_config = ClickHouseSettings()
