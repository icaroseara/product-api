# Product REST API

## Build docker images
```sh
docker-compose build
```

## Run docker containers in background
```sh
docker-compose up -d
```

## Health check
Make HTTP request using curl:
```sh
curl -X GET http://localhost:5000/
```
Expected response:
```sh
{
  "active_primary_shards": 0,
  "active_shards": 0,
  "active_shards_percent_as_number": 100.0,
  "cluster_name": "elasticsearch",
  "delayed_unassigned_shards": 0,
  "initializing_shards": 0,
  "number_of_data_nodes": 1,
  "number_of_in_flight_fetch": 0,
  "number_of_nodes": 1,
  "number_of_pending_tasks": 0,
  "relocating_shards": 0,
  "status": "green",
  "task_max_waiting_in_queue_millis": 0,
  "timed_out": false,
  "unassigned_shards": 0
}
```
