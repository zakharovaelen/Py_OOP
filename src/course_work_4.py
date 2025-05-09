import requests
import json
from abc import ABC, abstractmethod


class JobApi(ABC):
    @abstractmethod
    def fetch_vacancies(self, query):
        pass


class HHApi(JobApi):
    def fetch_vacancies(self, query):
        url = f'https://api.hh.ru/vacancies?text={query}'
        response = requests.get(url)
        return response.json().get('items', [])


class Vacancy:
    def __init__(self, title, link, salary, description):
        self.title = title
        self.link = link
        self.salary = salary if salary else 0  # Обработка случая, если salary None
        self.description = description
        self.validate()

    def validate(self):
        if not self.title or not self.link or not self.description:
            raise ValueError("Недостаточные данные для вакансии")

    def __lt__(self, other):
        return self.salary < other.salary

    def __repr__(self):
        return f"{self.title} - {self.salary} - {self.link}"


class VacancyStorage(ABC):
    @abstractmethod
    def save_vacancies(self, vacancies):
        pass

    @abstractmethod
    def load_vacancies(self):
        pass

    @abstractmethod
    def delete_vacancy(self, index):
        pass


class JsonVacancyStorage(VacancyStorage):
    def __init__(self, filename='vacancies.json'):
        self.filename = filename

    def save_vacancies(self, vacancies):
        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump([vars(v) for v in vacancies], file, ensure_ascii=False, indent=4)

    def load_vacancies(self):
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                data = json.load(file)
                return [Vacancy(
                    title=item.get('title'),
                    link=item.get('link'),
                    salary=item.get('salary', 0),  # Установите в 0, если salary отсутствует
                    description=item.get('description')
                ) for item in data]
        except FileNotFoundError:
            return []

    def delete_vacancy(self, index):
        vacancies = self.load_vacancies()
        if 0 <= index < len(vacancies):
            del vacancies[index]
            self.save_vacancies(vacancies)


def user_interface():
    api = HHApi()
    storage = JsonVacancyStorage()
    vacancies = storage.load_vacancies()

    while True:
        action = input(
            "Выберите действие: 1- Поиск вакансий, 2- Топ N, 3- Поиск по описанию, 4- Удалить вакансию, 5- Выход: ")

        if action == '1':
            query = input("Введите поисковый запрос: ")
            results = api.fetch_vacancies(query)

            for item in results:
                salary = item['salary']['from'] if item['salary'] else None
                vacancy = Vacancy(
                    title=item['name'],
                    link=item['alternate_url'],
                    salary=salary,
                    description=item['snippet']['requirement']
                )
                vacancies.append(vacancy)

            storage.save_vacancies(vacancies)

        elif action == '2':
            n = int(input("Введите количество вакансий (N): "))
            top_vacancies = sorted(vacancies, reverse=True)[:n]
            for v in top_vacancies:
                print(v)

        elif action == '3':
            keyword = input("Введите ключевое слово для поиска: ")
            filtered_vacancies = [v for v in vacancies if keyword.lower() in v.description.lower()]
            for fv in filtered_vacancies:
                print(fv)

        elif action == '4':
            index = int(input("Введите индекс вакансии для удаления: "))
            storage.delete_vacancy(index)

        elif action == '5':
            break


if __name__ == "__main__":
    user_interface()