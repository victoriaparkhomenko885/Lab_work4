
# ��������� �������� �������� 
import django
from django.db import models

# ��������� ������ ������� ��������
class HumiditySensor(models.Model):
    # ���� ��� ��������� ��������� �������� ��������
    current_humidity = models.IntegerField()
    # ���� ��� ��������� ������������� �������� ��������
    max_humidity = models.IntegerField()
    # ���� ��� ��������� ���������� �������� ��������
    min_humidity = models.IntegerField()
    # ���� ��� ��������� ���� ���������� ��������� �����
    last_updated = models.DateTimeField(auto_now=True)

    # ����� ��� ��������� ��������� �������� ��������
    def update_humidity(self, new_humidity):
        self.current_humidity = new_humidity
        # ��������� ����������� �� �������� �������� ��������, ���� ������� �������� ����������� �� ���
        if new_humidity > self.max_humidity:
            self.max_humidity = new_humidity
        elif new_humidity < self.min_humidity:
            self.min_humidity = new_humidity
        # �������� ����
        self.save()