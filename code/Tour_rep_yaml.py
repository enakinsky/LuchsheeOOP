import os
import yaml
from TourRepository import TourRepository
from TourRepositoryStrategy import TourRepFileStrategy
from Tour import Tour  # Импортируем класс Tour

class YamlTourRepFileStrategy(TourRepFileStrategy):
    def __init__(self, file_path: str):
        self.file_path = file_path

    def read(self):
        if not os.path.exists(self.file_path):
            return []
        with open(self.file_path, 'r', encoding='utf-8') as file:
            return yaml.safe_load(file) or []

    def write(self, data):
        with open(self.file_path, 'w', encoding='utf-8') as file:
            yaml.dump(data, file, allow_unicode=True, default_flow_style=False)

    def add(self, tour):
        data = self.read()
        data.append(tour.to_dict())
        self.write(data)

    def display(self):
        data = self.read()
        for item in data:
            print(item)

# Инициализация стратегии YAML
strategy = YamlTourRepFileStrategy('tours.yaml')

# Чтение данных из файла и отображение их
print("Current tours in YAML file:")
strategy.display()

# Создание репозитория с использованием стратегии YAML
yaml_repository = TourRepository(strategy)

# Создание нового тура
new_tour = Tour.create_new_tour(
            name="Золотое кольцо Абхазии",
            description="Однодневная экскурсия по всем достопримечательностям",
            price=2000,
            duration=5,
            climat="Субтропики"
            tour_code="5890000"
        )


yaml_repository.add_tour(new_tour)

yaml_repository.write_data()

# Отображение обновленного списка туров
print("\nUpdated tours in YAML file:")
strategy.display()
