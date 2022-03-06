from django.views import View
from django.http import JsonResponse, HttpResponse
import json
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
from django.core import serializers

from .models import CarModel, Car


@method_decorator(csrf_exempt, name='dispatch')
class GetApi(View):

    def get(self, request, id):
        if request.method == 'GET':
            if Car.objects.filter(manufacture_id=id).exists():
                cars = Car.objects.get(manufacture_id=id)
                car_model = CarModel.objects.get(pk=cars.car_model_id)
                dict_model = model_to_dict(car_model)

                model_data = {
                    'manufacturer': dict_model['manufacturer'],
                    'model_name': dict_model['model_name'],
                    'year_production': dict_model['year_production'],
                }

                cars_data = {
                    'Manufacture ID': cars.manufacture_id,
                    'Manufacturing Date': cars.manufacturing_date,
                    'Car Model': model_data,
                }

                return JsonResponse(cars_data, safe=False)
            else:
                return HttpResponse('Sorry, the car with ID ' + str(id) + ' doesn\'t exist')

        else:
            return HttpResponse('Operation NOT allowed')


@method_decorator(csrf_exempt, name='dispatch')
class PostApi(View):
    def post(self, request):
        if request.method == 'POST':

            data = json.loads(request.body.decode("utf-8"))
            data_car_manuf_id = data.get('manufacture_id')
            data_car_prod_date = data.get('production_date')
            data_car_model = data.get('car_model')

            data_car_model_manufacturer = data_car_model['manufacturer']
            data_car_model_name = data_car_model['model_name']
            data_car_model_year_production = data_car_model['year_production']

            try:
                car_model = CarModel.objects.get(manufacturer=data_car_model_manufacturer)
                car_model.model_name = data_car_model_name
                car_model.year_production = data_car_model_year_production
                car_model.save()

                car_data = {
                    'manufacture_id': data_car_manuf_id,
                    'manufacturing_date': data_car_prod_date,
                    'car_model': car_model,
                }

                if not Car.objects.filter(manufacture_id=data_car_manuf_id).exists():

                    Car.objects.create(**car_data)

                    dict_car_model = model_to_dict(car_model)
                    data = {
                        "message": "New car added with the following data",
                        "Car Data": {
                            'Manufacture ID': data_car_manuf_id,
                            'Manufacturing Date': data_car_prod_date,
                            'Car Model': {
                                'Manufacturer': dict_car_model['manufacturer'],
                                'Model Name': dict_car_model['model_name'],
                                'Year In Production': dict_car_model['year_production'],
                            }
                        },
                    }

                    return JsonResponse(data, status=201)
                else:
                    return HttpResponse('A car with this Manufacture ID already exists')

            except CarModel.DoesNotExist:
                car_model = CarModel.objects.create(manufacturer=data_car_model_manufacturer)
                car_model.model_name = data_car_model_name
                car_model.year_production = data_car_model_year_production
                car_model.save()

                car_data = {
                    'manufacture_id': data_car_manuf_id,
                    'manufacturing_date': data_car_prod_date,
                    'car_model': car_model,
                }

                Car.objects.create(**car_data)

                dict_car_model = model_to_dict(car_model)
                data = {
                    "message": "New car and new model added with the following data",
                    "Car Data": {
                        'Manufacture ID': data_car_manuf_id,
                        'Manufacturing Date': data_car_prod_date,
                        'Car Model': {
                            'Manufacturer': dict_car_model['manufacturer'],
                            'Model Name': dict_car_model['model_name'],
                            'Year In Production': dict_car_model['year_production'],
                        }
                    },
                }

                return JsonResponse(data, status=201)

        else:
            return HttpResponse('Operation NOT allowed')
