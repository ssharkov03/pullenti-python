﻿# SDK Pullenti Address, version 4.14, september 2022. Copyright (c) 2013, Pullenti. All rights reserved.
# Non-Commercial Freeware and Commercial Software.
# This class is generated using the converter Unisharping (www.unisharping.ru) from Pullenti C# project.
# The latest version of the code is available on the site www.pullenti.ru

from enum import IntEnum

class BusinessFactKind(IntEnum):
    """ Типы бизнес-фактов """
    UNDEFINED = 0
    CREATE = 1
    """ Создан """
    DELETE = 2
    """ Упразднён """
    GET = 3
    """ Приобретать, покупать """
    SELL = 4
    """ Продавать """
    HAVE = 5
    """ Владеть, иметь """
    PROFIT = 6
    """ Прибыль, доход """
    DAMAGES = 7
    """ Убытки """
    AGREEMENT = 8
    """ Соглашение """
    SUBSIDIARY = 9
    """ Дочернее предприятие """
    FINANCE = 10
    """ Финансировать, спонсировать """
    LAWSUIT = 11
    """ Судебный иск """
    
    @classmethod
    def has_value(cls, value):
        return any(value == item.value for item in cls)