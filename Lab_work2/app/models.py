
# Імпортуємо необхідні бібліотеки 
import django
from django.db import models

# Створюємо модель датчика вологості
class HumiditySensor(models.Model):
    # Поле для зберігання поточного значення вологості
    current_humidity = models.IntegerField()
    # Поле для зберігання максимального значення вологості
    max_humidity = models.IntegerField()
    # Поле для зберігання мінімального значення вологості
    min_humidity = models.IntegerField()
    # Поле для зберігання дати останнього оновлення даних
    last_updated = models.DateTimeField(auto_now=True)

    # Метод для оновлення поточного значення вологості
    def update_humidity(self, new_humidity):
        self.current_humidity = new_humidity
        # Оновлюємо максимальне та мінімальне значення вологості, якщо поточне значення відрізняється від них
        if new_humidity > self.max_humidity:
            self.max_humidity = new_humidity
        elif new_humidity < self.min_humidity:
            self.min_humidity = new_humidity
        # Зберігаємо зміни
        self.save()