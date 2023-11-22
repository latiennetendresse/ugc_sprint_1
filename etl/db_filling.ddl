-- NODE 1
CREATE DATABASE shard;
CREATE DATABASE replica;

CREATE TABLE shard.movie_views (id UUID DEFAULT generateUUIDv4(), user_id String, film_id String, viewed_frame Int64, event_time DateTime DEFAULT now()) Engine=ReplicatedMergeTree('/clickhouse/tables/shard1/movie_views', 'replica_1') PARTITION BY toYYYYMMDD(event_time) ORDER BY id;
CREATE TABLE replica.movie_views (id UUID DEFAULT generateUUIDv4(), user_id String, film_id String, viewed_frame Int64, event_time DateTime DEFAULT now()) Engine=ReplicatedMergeTree('/clickhouse/tables/shard2/movie_views', 'replica_2') PARTITION BY toYYYYMMDD(event_time) ORDER BY id;
CREATE TABLE default.movie_views (id UUID DEFAULT generateUUIDv4(), user_id String, film_id String, viewed_frame Int64, event_time DateTime DEFAULT now()) ENGINE = Distributed('company_cluster', '', movie_views, rand());

-- NODE 3

CREATE DATABASE shard;
CREATE DATABASE replica;

CREATE TABLE shard.movie_views (id UUID DEFAULT generateUUIDv4(), user_id String, film_id String, viewed_frame Int64, event_time DateTime DEFAULT now()) Engine=ReplicatedMergeTree('/clickhouse/tables/shard2/movie_views', 'replica_1') PARTITION BY toYYYYMMDD(event_time) ORDER BY id;
CREATE TABLE replica.movie_views (id UUID DEFAULT generateUUIDv4(), user_id String, film_id String, viewed_frame Int64, event_time DateTime DEFAULT now()) Engine=ReplicatedMergeTree('/clickhouse/tables/shard1/movie_views', 'replica_2') PARTITION BY toYYYYMMDD(event_time) ORDER BY id;
CREATE TABLE default.movie_views (id UUID DEFAULT generateUUIDv4(), user_id String, film_id String, viewed_frame Int64, event_time DateTime DEFAULT now()) ENGINE = Distributed('company_cluster', '', movie_views, rand());