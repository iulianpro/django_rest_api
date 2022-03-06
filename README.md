## Python/Django rest API

```bash
POST example: curl -X POST -H "Content-Type: application/json" http://127.0.0.1:8000/api/ -d "{\"manufacture_id\": \"car_15\", \"production_date\": \"2015-01-01\", \"car_model\": {\"manufacturer\": \"Porche\", \"model_name\": \"Cayene\", \"year_production\": 2001}}"
```

```bash
GET example: curl -X GET http://127.0.0.1:8000/api/car_19
```