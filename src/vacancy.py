import json


class Vacancy:
    """Класс для представления информации о вакансии"""

    def __init__(self, title, link, salary, description, address=None):
        self.title = title
        self.link = link
        self.description = description
        self.address = address
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
            except (ValueError, TypeError):
                self.min_salary = None
                self.max_salary = None

    def __str__(self):
        return f"{self.title}\nЗарплата: {self.salary}\nСсылка: {self.link}\nОписание: {self.description}\nАдресс: {self.address}"

    def __lt__(self, other):
        return self.min_salary < other.salary

    @staticmethod
    def from_json(json_str):
        data = json.loads(json_str)
        return Vacancy(data['title'], data['link'], data['salary'], data['description'], data['address'])


    # def to_json(self):
        #     return json.dumps(self.__dict__)

        # @staticmethod
        # def from_json(json_str):
        #     data = json.loads(json_str)
        #     return Vacancy(data['title'], data['link'], data['salary'], data['description'])
