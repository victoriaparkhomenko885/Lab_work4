# Імпортуємо тестовий модуль
import unittest

# Створюємо тестовий клас
class HumiditySensorTestCase(unittest.TestCase):
    # Створюємо тестовий екземпляр моделі
    def setUp(self):
        self.sensor = HumiditySensor(current_humidity=50, max_humidity=50, min_humidity=50)

    # Тестуємо метод оновлення поточного значення вологості
    def test_update_humidity(self):
        # Оновлюємо поточне значення вологості до 75
        self.sensor.update_humidity(75)
        # Перевіряємо, що поточне значення вологості дійсно змінилося
        self.assertEqual(self.sensor.current_humidity, 75)
        # Перевіряємо, що максимальне значення вологості дійсно змінилося
        self.assertEqual(self.sensor.max_humidity, 75)

# Запускаємо тест
if __name__ == '__main__':
    unittest.main()

