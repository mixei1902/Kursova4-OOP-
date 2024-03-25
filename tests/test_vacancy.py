import unittest
from unittest.mock import patch
from src.vacancy_save import JSONSaver
from src.vacancy import Vacancy


class TestJSONSaverClass(unittest.TestCase):
    @patch('builtins.open', create=True)
    def test_add_vacancy(self, mock_open):
        vacancy = Vacancy("Python Developer", "работа.ру", "100000-150000", "опыт от 3-х лет")
        json_saver = JSONSaver()

        json_saver.add_vacancy(vacancy)

        # Проверка, что метод open был вызван с ожидаемыми параметрами
        mock_open.assert_called_once_with('vacancies.json', 'a')


class TestVacancyClass(unittest.TestCase):
    def test_vacancy_creation(self):
        vacancy = Vacancy("Python Developer", "работа.ру", 100000-150000, "опыт от 3-х лет")

        self.assertEqual(vacancy.title, "Python Developer")
        self.assertEqual(vacancy.link, "работа.ру")
        self.assertEqual(vacancy.salary, 100000-150000)
        self.assertEqual(vacancy.description, "опыт от 3-х лет")

    def test_vacancy_creation_with_missing_salary(self):
        vacancy = Vacancy("Python Developer", "работа.ру", "", "опыт от 3-х лет")

        self.assertEqual(vacancy.salary, "Зарплата не указана")

    def test_vacancy_comparison(self):
        vacancy1 = Vacancy("Python Developer", "работа1.ру", 100000, "опыт от 3-х лет")
        vacancy2 = Vacancy("Python Developer", "eабота2.ру", 120000, "опыт от 4-х лет")

        self.assertLess(vacancy1, vacancy2)


if __name__ == '__main__':
    unittest.main()
