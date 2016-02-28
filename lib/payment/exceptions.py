class PurchaseError(BaseException):
    pass


class NoMoneyError(PurchaseError):
    pass
