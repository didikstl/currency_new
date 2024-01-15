from django.db.models.signals import pre_save
from django.dispatch import receiver
from account.models import User


@receiver(pre_save, sender=User)
def lower_user_email(instance, **kwargs):
    instance.email = instance.email.lower()


@receiver(pre_save, sender=User)
def isdigit_user_phone(sender, instance, *args, **kwargs):
    """
     Оставляем только цифры в номере телефона
    :param sender:
    :param instance:
    :param args:
    :param kwargs:
    :return:
    """
    instance.phone = ''.join(char for char in instance.phone if char.isdigit())
