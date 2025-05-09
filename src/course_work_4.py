import json
import requests
from abc import ABC, abstractmethod

class VacancyAPI(ABC):
    @abstractmethod
    def fetch_vacancies(self, query):
        pass

class HHruAPI(VacancyAPI):
    BASE_URL = 'https://api.hh.ru/vacancies'

    def fetch_vacancies(self, query):
        params = {'text': query, 'area': 113}  # Россия
        response = requests.get(self.BASE_URL, params=params)
        return response.json().get('items', [])

class Vacancy:
    def __init__(self, title, link, salary, description):
        self.title = title
        self.link = link
        self.salary = salary
        self.description = description

    def __lt__(self, other):
        return self.salary < other.salary

    def __repr__(self):
        return f"{self.title} - {self.salary} - {self.link}"

class VacancyStorage(ABC):
    @abstractmethod
    def add_vacancy(self, vacancy):
        pass

    @abstractmethod
    def get_vacancies(self, filter_func=None):
        pass

    @abstractmethod
    def remove_vacancy(self, vacancy):
        pass

class JSONVacancyStorage(VacancyStorage):
    def __init__(self, filename):
        self.vacancies = None
        self.filename = filename
        self.load_vacancies()

    def load_vacancies(self):
        try:
            with (open(self.filename, 'r', encoding='utf-8') as file):
                data = json.load(file)
                self.vacancies = []
                for item in data:
                    if isinstance(item, dict) and {"title", "link", "salary", "description"}.issubset(item.keys()):
                        self.vacancies.append(Vacancy(**item))
                    else:
                        print(f"Skipping invalid item: {item}")
        except FileNotFoundError:
            self.vacancies = []
        except json.JSONDecodeError as e:
                    print(f"Error reading JSON file: {e}")
                    self.vacancies = []

    def save_vacancies(self):
        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump([vars(vacancy) for vacancy in self.vacancies], file, ensure_ascii=False)

    def add_vacancy(self, vacancy):
        self.vacancies.append(vacancy)
        self.save_vacancies()

    def get_vacancies(self, filter_func=None):
        return [vacancy for vacancy in self.vacancies if filter_func is None or filter_func(vacancy)]

    def remove_vacancy(self, vacancy):
        self.vacancies.remove(vacancy)
        self.save_vacancies()

def user_interface():
    storage = JSONVacancyStorage('vacancies.json')
    api = HHruAPI()

    while True:
        print("1. Поиск вакансий")
        print("2. Топ N вакансий по зарплате")
        print("3. Вакансии по ключевому слову")
        print("4. Выход")
        choice = input("Выберите действие: ")

        if choice == '1':
            query = input("Введите поисковый запрос: ")
            vacancies_data = api.fetch_vacancies(query)
            for item in vacancies_data:
                vacancy = Vacancy(item['name'], item['link'], item['salary']['from'] if item['salary'] else 0, item['snippet']['requirement'])
                storage.add_vacancy(vacancy)
            print("Вакансии добавлены.")

        elif choice == '2':
            N = int(input("Сколько топ вакансий по зарплате показать? "))
            top_vacancies = sorted(storage.get_vacancies(), reverse=True)[:N]
            print(top_vacancies)

        elif choice == '3':
            keyword = input("Введите ключевое слово: ")
            filtered_vacancies = storage.get_vacancies(lambda v: keyword.lower() in v.description.lower())
            print(filtered_vacancies)

        elif choice == '4':
            break

if __name__ == "__main__":
    user_interface()