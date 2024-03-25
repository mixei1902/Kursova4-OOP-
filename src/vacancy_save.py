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
        with open(self.file_path, 'a') as file:
            json.dump(vars(vacancy), file)
            file.write('\n')

    def delete_vacancy(self, vacancy):
        # Заглушка для удаления вакансии из файла
        pass

    def get_vacancies_by_criteria(self, criteria):
        # Заглушка для получения вакансий из файла по критериям
        pass
