# Перед любым запуском нужно создать сеть, если она еще не создана
```bash
  docker network create shared_network
```

# Как запускать через docker-compose


1. Скопировать /ugc_sprint_1/ugc_service/env/.docker.env как /ugc_sprint_1/ugc_service/env/.env
2. Перейти в директрорию ugc_sprint_1
```bash
cd ugc_sprint_1
```
3. Запустить сборку docker-compose
```bash
docker-compose -f docker-compose.yaml up
```
4. Сервис доступен по адресу https://127.0.0.1:445/api/openapi
5. Сервис Kafka доступен по адресу http://127.0.0.1:9021/clusters

# Как запускать локально через Run Configuration

1. Скопировать /ugc_sprint_1/ugc_service/env/.local.env как /ugc_sprint_1/ugc_service/env/.env
2. Перейти в директрорию ugc_sprint_1
```bash
cd ugc_sprint_1
```
3. Запустить сборку docker-compose local
```bash
docker-compose -f docker-compose-local.yaml up
```
4. Настроить Run Configuration и запустить
5. Сервис доступен по адресу http://127.0.0.1:8000/api/openapi
6. Сервис Kafka доступен по адресу http://127.0.0.1:9021/clusters
