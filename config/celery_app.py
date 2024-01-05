from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Установите переменную окружения 'DJANGO_SETTINGS_MODULE' перед запуском Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings.settings')

# Создайте экземпляр Celery и настройте его, используя файл настроек Django
celery_app = Celery('currency_new')

# Загрузите конфигурацию для Celery из настроек Django
celery_app.config_from_object('django.conf:settings', namespace='CELERY')

# Автоматический поиск и загрузка задач из файла tasks.py в приложениях Django
celery_app.autodiscover_tasks()