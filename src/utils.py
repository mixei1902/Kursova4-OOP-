def filter_vacancies(vacancies, filter_words):
    """Фильтрует вакансии на основе указанных ключевых слов:"""
    return [vacancy for vacancy in vacancies if
            any(word.lower() in vacancy.get('description', '').lower() for word in filter_words)]



def get_vacancies_by_salary(vacancies, salary_range):
    """Фильтрация вакансий на основе диапазона зарплат"""
    if not salary_range:
        return vacancies
    salary_range = salary_range.split('-')
    if len(salary_range) == 1:
        min_salary = max_salary = int(salary_range[0])
    elif len(salary_range) == 2:
        min_salary, max_salary = map(int, salary_range)
    else:
        print("Неверный формат диапазона зарплат.")
        return vacancies

    return [vacancy for vacancy in vacancies if
            vacancy.get('salary_from', 0) >= min_salary and vacancy.get('salary_from', float('inf')) <= max_salary]


def sort_vacancies(vacancies):
    """Сортирует вакансии на основе зарплаты в порядке убывания"""
    return sorted(vacancies, key=lambda vacancy: vacancy.get('salary_from', 0), reverse=True)


def get_top_vacancies(vacancies, top_n):
    """Возвращает N вакансий из списка"""
    return vacancies[:top_n]


def print_vacancies(vacancies):
    if vacancies:
        for index, vacancy in enumerate(vacancies, start=1):
            print(f"Вакансия {index}:")
            print(f"Название: {vacancy.get('name', 'Не указано')}")
            print(f"Зарплата от: {vacancy.get('salary_from', 'Не указана')}")
            print(f"Описание: {vacancy.get('description', 'Отсутствует')}")
            print(f"Ссылка: {vacancy.get('alternate_url', 'Не указана')}")
            print()
    else:
        print("Нет подходящих вакансий")
