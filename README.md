# Product Catalog REST API

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
curl -X GET http://0.0.0.0:5000/api/healthcheck
```
Expected response:
```sh
{
	"hostname": "products_api",
	"status": "success",
	"timestamp": 1518735844.6434016,
	"results": [{
		"checker": "elasticsearch_available",
		"output": "elasticsearch ok",
		"passed": true,
		"timestamp": 1518735844.6427352,
		"expires": 1518735871.6427352
	}]
}
```

## Products API

### Fetch Product by SKU
TODO

### Fetch Product by category
TODO
### Fetch Product by date added
TODO

### Create Product
Make HTTP request using curl:
```sh
curl -d '{ "brand": "Marvel", "categories": [ "Super Heroes", "Flying Cars", "Cars" ], "name": "Batmobile", "price": "122.99", "product_image_url": "http://static.dafiti.com.br/9527534/1-zoom.jpg", "sku": "BATMAN-123", "type": "accessories" }' -H "Content-Type: application/json" -X POST  http://0.0.0.0:5000/api/v1/products
```
Expected response:
```sh
{
  "brand": "Marvel",
  "categories": [
    "Super Heroes",
    "Flying Cars",
    "Cars"
  ],
  "created_at": "2018-02-15T23:38:04.031705",
  "name": "Batmobile",
  "price": "122.99",
  "product_image_url": "http://static.dafiti.com.br/9527534/1-zoom.jpg",
  "sku": "BATMAN-123",
  "type": "accessories"
}
```
