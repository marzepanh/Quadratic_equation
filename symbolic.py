from sympy import symbols, Eq, solve, simplify, I
from numbers import Number
from typing import Union, Optional, List
import math

def is_valid_number(val) -> bool:
    """Проверяет, является ли значение допустимым числом (включая комплексные),
    исключая булевы значения, бесконечности и NaN.
    """
    if isinstance(val, bool):
        return False
    if isinstance(val, complex):
        return not (math.isinf(val.real) or math.isnan(val.real) or
                    math.isinf(val.imag) or math.isnan(val.imag))
    if isinstance(val, Number):
        return not (math.isinf(val) or math.isnan(val))
    return False


def solve_equation(
    a_val: Optional[Union[int, float, complex]] = None,
    b_val: Optional[Union[int, float, complex]] = None,
    c_val: Optional[Union[int, float, complex]] = None,
    target: Optional[Union[int, float, complex]] = 7
) -> Union[str, List, list]:
    """
    Решает уравнение вида: ax² + bx + c = 7.
    Если переданы значения a, b, c, возвращает корни уравнения
    (в том числе комплексные, если они есть).
    Если значения не переданы, возвращает символьное общее решение.

    Параметры:
        a_val (int | float | complex | None): Коэффициент при x².
        b_val (int | float | complex | None): Коэффициент при x.
        c_val (int | float | complex | None): Свободный член.
        target: (int | float | complex | None) правая часть уравнения (по умолчанию 7).

    Возвращает:
        - Список корней (sympy expressions), если решение возможно.
        - Строку с описанием, если решений нет или введены некорректные значения.
        - Символьное решение, если параметры не заданы.
    """
    a, b, c, x = symbols('a b c x')

    if all(val is not None and is_valid_number(val) for val in (a_val, b_val, c_val, target)):

        left = a_val * x**2 + b_val * x + (c_val - target)

        if a_val == 0 and b_val == 0:
            if c_val == target:
                return "Бесконечно много решений (тождество 0 = 0)"
            else:
                return "Нет решений (противоречие вида 0 = число)"
        else:
            roots = solve(Eq(left, 0), x)
            return [simplify(r) for r in roots]
    else:
        return "Ошибка: параметры должны быть числами (включая комплексные, но не NaN/inf)."



print(solve_equation(0, 2, 5))