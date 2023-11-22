# Запуск ETL процесса

1.Развернуть Kafka и Clickhouse
```bash
docker compose -f docker-compose.yaml up --build
```
2. Зайти в контейнер кликхауса с нодой 1
```bash
docker exec -it clickhouse-node1 bash
```
3. Запустить command-Line client кликхауса
```bash
clickhouse-client
```
4. Выполнить запросы для NODE 1, описанные в __**_db_filling.ddl_**__
5. Зайти в контейнер с нодой 3
```bash
exit 
```
```bash
exit
```
```bash
docker exec -it clickhouse-node3 bash
```
6. Повторить шаг №3
7. Выполнить запросы для NODE 3, описанные в __**_db_filling.ddl_**__

8. Запустить процесс ETL, находясь в /etl
```bash
docker build -t etl_app .
```

```bash
docker run -d --name etl_app_container --network shared_network etl_app
```
