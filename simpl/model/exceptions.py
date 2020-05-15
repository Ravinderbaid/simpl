class ModelException(Exception):
    pass


class EmailException(ModelException):
    pass


class NameException(ModelException):
    pass


class UserException(ModelException):
    pass


class MerchantException(ModelException):
    pass


class TransactException(ModelException):
    pass


class InvalidDiscountException(MerchantException):
    pass


class InsufficientCreditException(UserException):
    pass


class InvalidPaybackAmountException(UserException):
    pass


class InvalidCreditLimitException(UserException):
    pass


class InvalidUserException(UserException):
    pass


class InvalidMerchantException(MerchantException):
    pass


class InvalidTransactionAmountException(TransactException):
    pass
