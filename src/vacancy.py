import json


class Vacancy:
    """Конструктор класса"""

    def __init__(self, title, link, salary, description):
        self.title = title
        self.link = link
        self.description = description
        if isinstance(salary, str) and '-' in salary:
            salary_range = salary.split('-')
            try:
                self.min_salary = int(salary_range[0])
                self.max_salary = int(salary_range[1])
            except ValueError:
                self.min_salary = None
                self.max_salary = None
        else:
            # Преобразуем зарплату в число, если это возможно
            try:
                self.min_salary = int(salary)
                self.max_salary = int(salary)
            except ValueError:
                self.min_salary = None
                self.max_salary = None

    def __str__(self):
        return f"{self.title}\nЗарплата: {self.salary}\nСсылка: {self.link}\nОписание: {self.description}\n"

    def __lt__(self, other):
        return self.min_salary < other.salary

    @staticmethod
    def from_json(json_str):
        data = json.loads(json_str)
        return Vacancy(data['title'], data['link'], data['salary'], data['description'])

    def to_json(self):
        return {
            "Название": self.title,
            "Описание": self.description or 'Описание отсутствует',
            "Ссылка": self.link or 'Не указана',
            "Зарплата от": self.min_salary if self.min_salary is not None else 'Не указана',
            "Зарплата до": self.max_salary if self.max_salary is not None else 'Не указана'
        }
        # def to_json(self):
        #     return json.dumps(self.__dict__)

        # @staticmethod
        # def from_json(json_str):
        #     data = json.loads(json_str)
        #     return Vacancy(data['title'], data['link'], data['salary'], data['description'])
