# ��������� �������� ������
import unittest

# ��������� �������� ����
class HumiditySensorTestCase(unittest.TestCase):
    # ��������� �������� ��������� �����
    def setUp(self):
        self.sensor = HumiditySensor(current_humidity=50, max_humidity=50, min_humidity=50)

    # ������� ����� ��������� ��������� �������� ��������
    def test_update_humidity(self):
        # ��������� ������� �������� �������� �� 75
        self.sensor.update_humidity(75)
        # ����������, �� ������� �������� �������� ����� ��������
        self.assertEqual(self.sensor.current_humidity, 75)
        # ����������, �� ����������� �������� �������� ����� ��������
        self.assertEqual(self.sensor.max_humidity, 75)

# ��������� ����
if __name__ == '__main__':
    unittest.main()

