import unittest
from symbolic import solve_equation
from sympy import simplify, sqrt, S, I

class TestQuadraticSolver(unittest.TestCase):
    def test_real_roots(self):
        # два действительных корня (x² - 3x - 5 = 0)
        result = solve_equation(1, -3, 2)
        expected = [S(3)/2 - sqrt(29)/2, S(3)/2 + sqrt(29)/2]
        self.assertEqual([simplify(r) for r in result], expected)

        # уравнение вида x² = 7
        result = solve_equation(1, 0, 0)
        expected = [-sqrt(7), sqrt(7)]
        self.assertEqual([simplify(r) for r in result], expected)

    def test_complex_roots(self):
        from sympy import im, re

        # Чисто мнимые корни (x² + 1 = 0 → x = ±i)
        result = solve_equation(1, 0, 1, target=0)
        self.assertEqual(len(result), 2)
        for r in result:
            self.assertTrue(r.has(I))
            self.assertEqual(re(r), 0)
            self.assertNotEqual(im(r), 0)

        # Общий комплексный случай (x² + x + 1 = 0)
        result = solve_equation(1, 1, 1, target=0)
        self.assertEqual(len(result), 2)
        for r in result:
            self.assertTrue(r.has(I))
            self.assertNotEqual(im(r), 0)

        # Комплексные коэффициенты (ix² + 2x + 3 = 0)
        result = solve_equation(1j, 2, 3, target=0)
        self.assertEqual(len(result), 2)
        for r in result:
            self.assertTrue(r.has(I) or isinstance(r, complex))
            if not isinstance(r, complex):
                self.assertTrue(r.is_complex)

    def test_special_cases(self):
        # бесконечно много решений
        self.assertEqual(solve_equation(0, 0, 7, 7),
                        "Бесконечно много решений (тождество 0 = 0)")

        # нет решений
        self.assertEqual(solve_equation(0, 0, 6),
                        "Нет решений (противоречие вида 0 = число)")

        # линейное уравнение (2x - 2 = 0)
        result = solve_equation(0, 2, 5)
        expected = [S(1)]
        self.assertEqual([simplify(r) for r in result], expected)

        # кратный корень (x² + 2x + 1 = 0)
        result = solve_equation(1, 2, 8)
        expected = [-1]
        self.assertEqual([simplify(r) for r in result], expected)

    def test_invalid_input(self):
        # неверные типы
        self.assertEqual(solve_equation("abc", 2, 5),
                        "Ошибка: параметры должны быть числами (включая комплексные, но не NaN/inf).")

        # None в аргументах
        self.assertEqual(solve_equation(None, 2, 3),
                        "Ошибка: параметры должны быть числами (включая комплексные, но не NaN/inf).")

        # булево значение
        self.assertEqual(solve_equation(True, 2, 3),
                        "Ошибка: параметры должны быть числами (включая комплексные, но не NaN/inf).")

    def test_edge_cases(self):
        # бесконечность
        self.assertEqual(solve_equation(float('inf'), 2, 3),
                        "Ошибка: параметры должны быть числами (включая комплексные, но не NaN/inf).")

        # NaN
        self.assertEqual(solve_equation(float('nan'), 2, 3),
                        "Ошибка: параметры должны быть числами (включая комплексные, но не NaN/inf).")

    def test_float_coefficients(self):
        # float коэффициенты
        result = solve_equation(1.5, 2.8, 6)
        self.assertEqual(len(result), 2)

if __name__ == '__main__':
    unittest.main()