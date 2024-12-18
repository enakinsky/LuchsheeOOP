from typing import List, Optional
from Tour import Tour
from BriefTour import BriefTour
from TourRepositoryStrategy import TourRepFileStrategy

class TourRepository:
    def __init__(self, strategy: TourRepFileStrategy):
        self._data = []
        self._strategy = strategy
        self.read_data()

    def write_data(self)
        self._strategy.write(self._data)

    def read_data(self):
        self._data = self._strategy.read()

    def add_tour(self, tour: Tour)
        tour_dict = tour.to_dict()
        tours = [Tour.create_from_dict(prod) for prod in self._data]
        if not self.check_unique_code(tour, tours):
            raise ValueError(f"Tour already exists.")
        self._data.append(tour_dict)

    def check_unique_code(self, tour, tours):
        for tour_data in tours:
            if tour_data == tour:
                 raise ValueError(f"Tour already exists.")
        return True

    def get_by_id(self, tour_id: int) -> Optional[Tour]:
        for tour in self._data:
            if tour['tour_id'] == tour_id:
                return Tour.create_from_dict(tour)
        return None

    def get_k_n_short_list(self, k: int, n: int) -> List[BriefTour]:
        start_index = (n - 1) * k
        end_index = start_index + k
        return [
            BriefTour(
                tour_id=tour['tour_id'],
                name=tour['name'],
                price=tour['price'],
                tour_code=tour['tour_code']
            )
            for tour in self._data[start_index:end_index]
        ]

    def sort_by_field(self, field: str, reverse: bool = False) -> List[Tour]:
        if field not in ['tour_id', 'name', 'price', 'duration', 'climat', 'tour_code']:
            raise ValueError(f"Invalid field '{field}' for sorting.")
        self._data.sort(key=lambda x: x.get(field), reverse=reverse)
        return [Tour.create_from_dict(tour) for tour in self._data]

    def tour_replace_by_id(self, tour_id: int, name=None, description=None, price=None,
                               duration=None, climat=None, tour_code=None):
        tour = self.get_by_id(tour_id)
        if not tour:
            raise ValueError(f"Tour with ID {tour_id} not found.")

        tours = [Tour.create_from_dict(prod) for prod in self._data]
        if not self.check_unique_code(tour, tours):
            raise ValueError(f"Tour already exists.")

        if name:
            tour.name = name
        if description:
            tour.description = description
        if price:
            tour.price = price
        if stock_quantity:
            tour.stock_quantity = stock_quantity
        if material:
            tour.material = material
        if tour_code:
            tour.tour_code = tour_code

        for i, p in enumerate(self._data):
            if p['tour_id'] == tour_id:
                self._data[i] = tour.to_dict()
                break

    def tour_delete_by_id(self, tour_id: int):
        tour = self.get_by_id(tour_id)
        if not tour:
            raise ValueError(f"Tour with ID {tour_id} not found.")
        self._data = [p for p in self._data if p['tour_id'] != tour_id]

    def get_count(self) -> int:
        return len(self._data)



