def filter_vacancies(vacancies, filter_words):
    """Фильтрует вакансии на основе указанных ключевых слов"""
    return [vacancy for vacancy in vacancies if
            any(word.lower() in vacancy.description.lower() for word in filter_words)]


def get_vacancies_by_salary(vacancies, salary_range):
    """Фильтрация вакансий на основе диапазона зарплат"""
    if not salary_range:
        return vacancies

    min_salary, max_salary = map(int, salary_range.split('-'))

    return [vacancy for vacancy in vacancies if
            (vacancy.salary >= min_salary if vacancy.salary is not None else False) and
            (vacancy.salary <= max_salary if vacancy.salary is not None else False)]


def sort_vacancies(vacancies):
    """Сортирует вакансии на основе зарплаты в порядке убывания"""
    return sorted(vacancies, key=lambda vacancy: vacancy.salary or 0, reverse=True)


def get_top_vacancies(vacancies, top_n):
    """Возвращает N вакансий из списка"""
    return vacancies[:top_n]


def print_vacancies(vacancies):
    if vacancies:
        for index, vacancy in enumerate(vacancies, start=1):
            print(f"Вакансия {index}:")
            print(f"Название: {vacancy.title}")
            print(f"Зарплата от: {vacancy.salary or 'Не указана'}")
            print(f"Описание: {vacancy.description or 'Отсутствует'}")
            print(f"Ссылка: {vacancy.link or 'Не указана'}")
            print()
    else:
        print("Нет подходящих вакансий")
