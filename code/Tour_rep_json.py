import json
import os
from Tour import Tour
from TourRepository import TourRepository
from TourRepositoryStrategy import TourRepFileStrategy

class JsonTourRepFileStrategy(TourRepFileStrategy):
    def __init__(self, file_path: str):
        self.file_path = file_path

    def read(self):
        if not os.path.exists(self.file_path):
            return []
        with open(self.file_path, 'r', encoding='utf-8') as file:
            return json.load(file)

    def write(self, data):
        with open(self.file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def display(self):
        data = self.read()
        for item in data:
            print(item)
            
strategy = JsonTourRepFileStrategy('tours.json')

json_repository = TourRepository(strategy)

new_tour = Tour.create_new_tour(
            name="Золотое кольцо Абхазии",
            description="Однодневная экскурсия по всем достопримечательностям",
            price=2000,
            duration=5,
            climat="Субтропики"
            tour_code="5890000"
        )

for tour in json_repository.get_k_n_short_list(1,1):
    print(tour)


print("\nUpdated tours in JSON file:")
strategy.display()
