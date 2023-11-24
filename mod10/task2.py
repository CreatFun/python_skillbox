import re
import doctest


def is_date_correct(date: str) -> bool:
    """
    >>> is_date_correct('20 января 1806')
    True
    >>> is_date_correct('1924, July 25')
    True
    >>> is_date_correct('26/09/1635')
    True
    >>> is_date_correct('3.1.1506')
    True
    >>> is_date_correct('25.08-1002')
    False
    >>> is_date_correct('декабря 19, 1838')
    False
    >>> is_date_correct('8.20.1973')
    False
    >>> is_date_correct('Jun 7, -1563')
    False
    >>> is_date_correct('31 февраля 2023')
    False
    >>> is_date_correct('31 июня 2015')
    False
    """

    date_pattern = (r'^(?:(?:0?\d|[12]\d|3[01])([\.\/-])(?:(?<!3[01][\.\/-])0?2|(?<!31[\.\/-])0?[469]|0?['
                    r'^2469]|12)\1\d{4}|\d{4}([\.\/-])(?:0?2(?![\.\/-]3[01])|0?[469](?!31[\.\/-])|0?[^2469]|12)\2('
                    r'?:0?\d|[12]\d|3[01])|(?:[0-2]\d|3[01]) (?:января|(?<!3[01] )февраля|марта|(?<!31 )('
                    r'?:апреля|июня|сентября|ноября)|мая|июля|августа|октября|декабря) \d{4}|(?:Jan(?:uary)?|Feb('
                    r'?:ruary)?(?! 3[01])|Mar(?:ch)?|(?:Apr(?:il)?|June?|Sep(?:tember)?|Nov(?:ember)?)(?! '
                    r'31)|May|July?|Aug(?:ust)?|Oct(?:ober)?|Dec(?:ember)?) (?:[0-2]\d|3[01]), \d{4}|\d{4}, '
                    r'(?:Jan(?:uary)?|Feb(?:ruary)?(?! 3[01])|Mar(?:ch)?|(?:Apr(?:il)?|June?|Sep(?:tember)?|Nov('
                    r'?:ember)?)(?! 31)|May|July?|Aug(?:ust)?|Oct(?:ober)?|Dec(?:ember)?) (?:[0-2]\d|3[01]))$')

    return bool(re.match(date_pattern, date))


doctest.testmod(verbose=True)
