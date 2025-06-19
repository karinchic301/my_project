"""
Пример простого модуля с функциями калькулятора.

Этот модуль будет использован для демонстрации автоматической генерации документации.
"""

def add(a: float, b: float) -> float:
    """
    Возвращает сумму двух чисел.

    Args:
        a (float): Первое число.
        b (float): Второе число.

    Returns:
        float: Сумма чисел a и b.
    """
    return a + b

def multiply(a: float, b: float) -> float:
    """
    Возвращает произведение двух чисел.

    Args:
        a (float): Первое число.
        b (float): Второе число.

    Returns:
        float: Произведение чисел a и b.
    """
    return a * b

def subtract(a: float, b: float) -> float:
    """
    Возвращает разность двух чисел.

    Args:
        a (float): Уменьшаемое.
        b (float): Вычитаемое.

    Returns:
        float: Результат вычитания b из a.
    """
    return a - b
