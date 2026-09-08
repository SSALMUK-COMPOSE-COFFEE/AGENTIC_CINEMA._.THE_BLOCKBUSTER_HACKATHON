CREATE DATABASE IF NOT EXISTS shot_memory;

CREATE TABLE IF NOT EXISTS shot_memory.films
(
    film_id     String,
    title       String,
    year        UInt16,
    source_uri  String,
    fps         Float32,
    duration    Float64,
    shot_count  UInt32 DEFAULT 0,
    status      Enum8('pending'=0,'detecting'=1,'describing'=2,'embedding'=3,'loading'=4,'done'=5,'failed'=6) DEFAULT 'pending',
    created_at  DateTime DEFAULT now(),
    updated_at  DateTime DEFAULT now()
)
ENGINE = ReplacingMergeTree(updated_at)
ORDER BY film_id;

CREATE TABLE IF NOT EXISTS shot_memory.shots
(
    film_id          LowCardinality(String),
    film_title       String,
    shot_id          String,
    shot_index       UInt32,
    t_in             Float64,
    t_out            Float64,
    duration         Float64 MATERIALIZED t_out - t_in,
    caption          String,
    people_count     UInt8,
    time_of_day      Enum8('unknown'=0,'day'=1,'night'=2,'dawn'=3,'dusk'=4),
    interior         Enum8('unknown'=0,'interior'=1,'exterior'=2),
    weather          LowCardinality(String),
    shot_size        Enum8('unknown'=0,'ecu'=1,'cu'=2,'mcu'=3,'ms'=4,'mls'=5,'ls'=6,'els'=7),
    camera_move      LowCardinality(String),
    emotion          LowCardinality(String),
    tension          UInt8,
    dialogue_present Bool,
    dominant_colors  Array(String),
    objects          Array(String),
    characters       Array(String),
    thumbnail_uri    String,
    proxy_uri        String,
    embedding        Array(Float32),
    ingested_at      DateTime DEFAULT now(),
    INDEX emb_idx embedding TYPE vector_similarity('hnsw', 'cosineDistance', 3072)
)
ENGINE = MergeTree
ORDER BY (film_id, shot_index);

CREATE TABLE IF NOT EXISTS shot_memory.query_vectors
(
    query_id    String,
    embedding   Array(Float32),
    created_at  DateTime DEFAULT now()
)
ENGINE = MergeTree
ORDER BY query_id
TTL created_at + INTERVAL 1 DAY;

CREATE TABLE IF NOT EXISTS shot_memory.sequences
(
    sequence_id  String,
    session_id   String,
    intent       String,
    shot_ids     Array(String),
    approved     Bool DEFAULT false,
    created_at   DateTime DEFAULT now()
)
ENGINE = MergeTree
ORDER BY (session_id, created_at);

CREATE TABLE IF NOT EXISTS shot_memory.search_log
(
    session_id  String,
    query_text  String,
    sql_text    String,
    result_ids  Array(String),
    latency_ms  UInt32,
    created_at  DateTime DEFAULT now()
)
ENGINE = MergeTree
ORDER BY (session_id, created_at);
