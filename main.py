from abc import ABC, abstractmethod

import json
import requests


class JobAPI(ABC):
    @abstractmethod
    def get_jobs(self, query):
        pass


class HHAPI(JobAPI):
    def __init__(self):
        self.url = "https://api.hh.ru/vacancies"

    def get_jobs(self, query):
        params = {"text": query, "area": "1"}  # area 1 is for Russia
        response = requests.get(self.url, params=params)
        return response.json()


class Job:
    def __init__(self, title, url, salary, description):
        self.title = title
        self.url = url
        self.salary = self.validate_salary(salary)
        self.description = description

    def validate_salary(self, salary):
        if salary is None or salary == "":
            return "Зарплата не указана"
        else:
            return salary

    def __lt__(self, other):
        if isinstance(other, Job):
            return self.salary < other.salary

    def __eq__(self, other):
        if isinstance(other, Job):
            return self.salary == other.salary


class JobStorage(ABC):
    @abstractmethod
    def add_job(self, job):
        pass

    @abstractmethod
    def get_jobs(self, criteria):
        pass

    @abstractmethod
    def delete_jobs(self, criteria):
        pass


class JSONJobStorage(JobStorage):
    def __init__(self, filename):
        self.filename = filename

    def add_job(self, job):
        jobs = self.get_jobs({})
        jobs.append(job.__dict__)
        with open(self.filename, 'w') as f:
            json.dump(jobs, f)

    def get_jobs(self, criteria):
        try:
            with open(self.filename, 'r') as f:
                jobs = json.load(f)
        except FileNotFoundError:
            jobs = []
        return [job for job in jobs if all(item in job.items() for item in criteria.items())]

    def delete_jobs(self, criteria):
        jobs = self.get_jobs({})
        jobs = [job for job in jobs if not all(item in job.items() for item in criteria.items())]
        with open(self.filename, 'w') as f:
            json.dump(jobs, f)


def interact():
    api = HHAPI()
    storage = JSONJobStorage('jobs.json')

    while True:
        print("1. Ввести поисковый запрос для запроса вакансий из hh.ru")
        print("2. Получить топ N вакансий по зарплате")
        print("3. Получить вакансии с ключевым словом в описании")
        print("4. Выход")
        choice = input("Выберите действие: ")

        if choice == '1':
            query = input("Введите поисковый запрос: ")
            jobs_data = api.get_jobs(query)
            for job_data in jobs_data['items']:
                job = Job(job_data['name'], job_data['url'], job_data['salary'], job_data['snippet']['requirement'])
                storage.add_job(job)
            print("Вакансии добавлены в файл.")
        elif choice == '2':
            n = int(input("Введите количество вакансий: "))
            jobs = storage.get_jobs({})
            jobs.sort(reverse=True)
            for job in jobs[:n]:
                print(f"Название: {job['title']}, Зарплата: {job['salary']}, Ссылка: {job['url']}")
        elif choice == '3':
            keyword = input("Введите ключевое слово: ")
            jobs = storage.get_jobs({})
            for job in jobs:
                if keyword in job['description']:
                    print(f"Название: {job['title']}, Зарплата: {job['salary']}, Ссылка: {job['url']}")
        elif choice == '4':
            break
        else:
            print("Неверный выбор. Пожалуйста, попробуйте еще раз.")
