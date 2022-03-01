from django.shortcuts import render


from django.views import View
from django.http import JsonResponse, HttpResponse
import json
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from .models import CarModel, Car


@method_decorator(csrf_exempt, name='dispatch')
class Api(View):

    def post(self, request):
        if request.method == 'POST':

            data = json.loads(request.body.decode("utf-8"))
            car_model = data.get('car_model')
            car_manuf_id = data.get('manufacture_id')
            car_prod_date = data.get('production_date')

            car_data = {
                'car_model': car_model,
                'car_manufacture_id': car_manuf_id,
                'car_production_date': car_prod_date,
            }

            cart_item = Car.objects.create(**car_data)

            data = {
                "message": f"New item added to Cart with id: {cart_item.id}"
            }
            return JsonResponse(data, status=201)

    def get(self, request, id):
        if request.method == 'GET':
            cars_count = Car.objects.filter(manufacture_id=id).count()
            cars = Car.objects.filter(manufacture_id=id)
            cars_data = []

            for car in cars:
                cars_data.append({
                    'car_model': car.car_model.manufacturer,
                    'car_manufacture_id': car.manufacture_id,
                    'car_production_date': car.manufacturing_date,
                })

            data = {
                'cars': cars_data,
                'count': cars_count,
            }

        return JsonResponse(data)


class NoApi(View):
    def get(self, request):

        return HttpResponse('Not Allowed')
