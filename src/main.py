import json

from src.APIHeadHunter import HeadHunterAPI
from src.utils import filter_vacancies, get_vacancies_by_salary, sort_vacancies, get_top_vacancies
from src.utils import print_vacancies
from src.vacancy import Vacancy
from src.vacancy_save import JSONSaver


def user_interaction():
    search_query = input("Введите поисковый запрос: ")
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    salary_range = input("Введите диапазон зарплат (пример: 100000-150000): ")
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ")

    hh_api = HeadHunterAPI()
    hh_vacancies = hh_api.get_vacancies(search_query)

    if hh_vacancies and 'items' in hh_vacancies:
        print("Список вакансий получен.")
        vacancies_list = []
        for vacancy_info in hh_vacancies['items']:
            if isinstance(vacancy_info, dict):
                name = vacancy_info.get('name', 'Не указано')
                alternate_url = vacancy_info.get('alternate_url', 'Не указано')
                salary_info = vacancy_info.get('salary')
                if salary_info:
                    salary_from = salary_info.get('from', 'Зарплата не указана')
                else:
                    salary_from = 'Зарплата не указана'
                description = vacancy_info.get('snippet', {}).get('responsibility', 'Описание отсутствует')
                address = vacancy_info.get('address', 'Адрес не указан')
                vacancy = Vacancy(name, alternate_url, salary_from, description, address)
                vacancies_list.append(vacancy)
            elif isinstance(vacancy_info, Vacancy):
                vacancies_list.append(vacancy_info)

        filtered_vacancies = filter_vacancies(vacancies_list, filter_words)
        ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)
        sorted_vacancies = sort_vacancies(ranged_vacancies)
        top_vacancies = get_top_vacancies(sorted_vacancies, top_n)

        # Используем класс JSONSaver для сохранения вакансий
        json_saver = JSONSaver()
        for vacancy in top_vacancies:
            json_saver.add_vacancy(vacancy)

        print_vacancies(top_vacancies)
    else:
        print("Не удалось получить вакансии. Пожалуйста, проверьте запрос и попробуйте снова.")


if __name__ == "__main__":
    user_interaction()
    print("Программа завершила выполнение.")
