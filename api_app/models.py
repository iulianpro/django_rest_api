from django.db import models


class CarModel(models.Model):
    manufacturer = models.CharField(max_length=50)
    model_name = models.CharField(max_length=50)
    year_production = models.DateField()

    def __str__(self):
        return "Manufacturer: {0}, Model: {1}, Yesr in production: {2}" \
            .format(self.manufacturer, self.model_name, self.year_production)


class Car(models.Model):
    car_model = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    manufacture_id = models.TextField()
    manufacturing_date = models.DateField()

    def __str__(self):
        return "Manufacture ID: {0}, Manufacturer: {1}, Model {2}" \
            .format(self.manufacture_id, self.car_model.manufacturer, self.car_model.model_name)
