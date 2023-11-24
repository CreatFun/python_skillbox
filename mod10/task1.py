import re
import doctest


def is_password_correct(password: str) -> bool:
    """
    >>> is_password_correct('rtG&3FG#Tr^e')
    True
    >>> is_password_correct('a^A1@*@1Aa')
    True
    >>> is_password_correct('oF^a1D@y5%e6')
    True
    >>> is_password_correct('enroi#$*rkdeR#$*092uwedchf34tguv394h')
    True
    >>> is_password_correct('пароль')
    False
    >>> is_password_correct('password')
    False
    >>> is_password_correct('qwerty')
    False
    >>> is_password_correct('lOngPa$$W0Rd')
    False
    """

    password_pattern = (
        r'^(?=[A-Za-z\d^$%@#&*]{8,})'  # только латинские символы, цифры и специальные символы ^$%@#&*, не менее 8 символов
        r'(?=(?:.*[a-z].*){2,})'  # по крайней мере два латинских символа в нижнем регистре
        r'(?=(?:.*[1-9].*){1,})'  # по крайней мере одна цифра
        r'(?=[^,.!?]*$).*([\^$%@#&*]).*(?!\1)'  # не содержит символы ,.!?
        r'([\^$%@#&*]).*(?!\1)(?!\2)([\^$%@#&*]).*$')

    return bool(re.match(password_pattern, password))


doctest.testmod(verbose=True)
