def filter_vacancies(vacancies, ключевые_слова):
    return [вакансия for вакансия in vacancies if
            any(ключ.lower() in вакансия['description'].lower() for ключ in ключевые_слова)]


def get_vacancies_by_salary(vacancies, диапазон_зарплат):
    if not диапазон_зарплат:
        return vacancies
    значения_зарплаты = диапазон_зарплат.split('-')
    if len(значения_зарплаты) == 1:
        мин_зарплата = макс_зарплата = int(значения_зарплаты[0])
    elif len(значения_зарплаты) == 2:
        мин_зарплата, макс_зарплата = map(int, значения_зарплаты)
    else:
        print("Неверный формат диапазона зарплат.")
        return vacancies

    return [вакансия for вакансия in vacancies if
            вакансия.get('salary_from', 0) >= мин_зарплата and вакансия.get('salary_from',
                                                                            float('inf')) <= макс_зарплата]


def sort_vacancies(vacancies):
    return sorted(vacancies, key=lambda вакансия: вакансия.get('salary_from', 0), reverse=True)


def get_top_vacancies(vacancies, верхняя_граница):
    return vacancies[:верхняя_граница]


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

