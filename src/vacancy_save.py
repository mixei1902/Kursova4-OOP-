import json
from abc import ABC, abstractmethod


class AbstractVacancySaver(ABC):
    @abstractmethod
    def add_vacancy(self, vacancy):
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy):
        pass

    @abstractmethod
    def get_vacancies_by_criteria(self, criteria):
        pass


class JSONSaver(AbstractVacancySaver):
    """Класс сохранения данных в json файл"""

    def __init__(self, file_path="vacancies.json"):
        self.file_path = file_path

    def add_vacancy(self, vacancy):
        with open(self.file_path, 'a', encoding='utf-8') as file:
            vacancy_info = {
                "Название": vacancy.title,
                "Ссылка": vacancy.link,
                "Зарплата": f"{vacancy.min_salary}-{vacancy.max_salary}" if vacancy.max_salary is not None else vacancy.min_salary,
                "Описание": vacancy.description,
                "Адрес": vacancy.address if vacancy.address is not None else "Не указан"
            }
            json.dump(vacancy_info, file, ensure_ascii=False)
            file.write('\n')

    def delete_vacancy(self, vacancy):
        # Заглушка для удаления вакансии из файла
        pass

    def get_vacancies_by_criteria(self, criteria):
        # Заглушка для получения вакансий из файла по критериям
        pass