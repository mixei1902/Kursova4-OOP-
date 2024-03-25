from abc import ABC, abstractmethod

import requests


class AbstractAPI(ABC):
    @abstractmethod
    def get_vacancies(self, search_query):
        pass


class HeadHunterAPI(AbstractAPI):
    def __init__(self):
        self.base_url = "https://api.hh.ru/vacancies"

    def get_vacancies(self, search_query):
        params = {"text": search_query, "area": 1}  # Здесь 1 - это код региона (Москва)
        response = requests.get(self.base_url, params=params)
        return response.json()
