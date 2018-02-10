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
  "healthy": true
}
```
