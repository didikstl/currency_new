# from __future__ import absolute_import, unicode_literals
# import os
# from celery import Celery
# from config import settings
#
# # Установите переменную окружения 'DJANGO_SETTINGS_MODULE' перед запуском Celery
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'currency_new.config.settings')
#
# # Создайте экземпляр Celery и настройте его, используя файл настроек Django
# celery_app = Celery('currency_new')
#
# # Загрузите конфигурацию для Celery из настроек Django
# celery_app.config_from_object('django.conf:settings', namespace='CELERY')
#
# # Автоматический поиск и загрузка задач из файла tasks.py в приложениях Django
# # celery_app.autodiscover_tasks(['app.currency_new'])
# celery_app.autodiscover_tasks()
#
# from app.currency.tasks import debug_task
#
# result = celery_app.send_task('app.currency.tasks.debug_task')


# from __future__ import absolute_import, unicode_literals
# import os
# from celery import Celery
# from config import settings
#
# # Установите переменную окружения 'DJANGO_SETTINGS_MODULE' перед запуском Celery
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'currency_new.config.settings')
#
# # Создайте экземпляр Celery и настройте его, используя файл настроек Django
# celery_app = Celery('currency_new')
#
# # Загрузите конфигурацию для Celery из настроек Django
# celery_app.config_from_object('django.conf:settings', namespace='CELERY')
#
# # Автоматический поиск и загрузка задач из файла tasks.py в приложениях Django
# celery_app.autodiscover_tasks()
#
# if __name__ == '__main__':
#     # Этот блок будет выполнен только при явном запуске celery.py
#     from app.currency.tasks import debug_task
#
#     # Вызов задачи
#     result = debug_task.delay()


# from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'currency_new.config.settings')

celery_app = Celery('currency_new')
celery_app.config_from_object('django.conf:settings', namespace='CELERY')
celery_app.autodiscover_tasks()
