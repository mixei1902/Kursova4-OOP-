import json


class Vacancy:
    """Конструктор класса"""
    def __init__(self, title, link, salary, description):
        self.title = title
        self.link = link
        self.salary = salary
        self.description = description

        # Валидация данных
        if not isinstance(self.salary, (str, int, float)):
            self.salary = "Зарплата не указана"

    def __str__(self):
        return f"{self.title}\nЗарплата: {self.salary}\nСсылка: {self.link}\nОписание: {self.description}\n"

    def __lt__(self, other):
        return self.salary < other.salary

    def to_json(self):
        return json.dumps(self.__dict__)

    @staticmethod
    def from_json(json_str):
        data = json.loads(json_str)
        return Vacancy(data['title'], data['link'], data['salary'], data['description'])
