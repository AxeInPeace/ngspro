# coding=utf-8
from django.contrib.contenttypes.fields import ContentType

from lib.payment.exceptions import NoMoneyError, PurchaseError
from lib.payment.models import Payment, Cost


class PurchaseableMixin:
    """
    Mixin для создания функциональности покупаемого объекта
    """

    def __init__(self):
        pass

    def buy(self, user):
        obj_type = ContentType.objects.get_for_model(self)
        cost = Cost.objects.filter(content_type=obj_type).first()
        if cost is None:
            raise PurchaseError
        elif user.customuser.cash >= cost.cost:
            raise NoMoneyError
        payment, created = Payment.objects.get_or_create(user=user, content_type__pk=obj_type,
                                                         object_id=self.pk, sum=cost.cost)
        return payment
