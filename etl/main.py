from clickhouse_driver import Client
import time

from src.core.settings import clickhouse_config, kafka_config
from src.read_from_kafka import KafkaReader
from src.write_to_clickhouse import ClickHouseWriter


def main():
    with KafkaReader(kafka_config) as kafka, ClickHouseWriter(clickhouse_config) as clickhouse:
        messages = []
        last_received_time = time.time()

        while True:
            for message in kafka.get_data():
                messages.append(message)
                if len(messages) >= kafka_config.batch_size or (time.time() - last_received_time) >= 5:
                    clickhouse.write_data(messages)
                    kafka.commit()
                    messages.clear()


if __name__ == '__main__':
    client = Client(host=clickhouse_config.clickhouse_host)
    main()
