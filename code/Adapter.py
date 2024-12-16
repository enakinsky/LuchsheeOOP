from TourRepository import  TourRepository

class TourRepositoryAdapter:

    def __init__(self, tour_repository: TourRepository):
        self._tour_repository = tour_repository

    def get_k_n_short_list(self, k, n):
        return self._tour_repository.get_k_n_short_list(k, n)

    def get_by_id(self, tour_id):
        return self._tour_repository.get_by_id(tour_id)

    def delete_by_id(self, tour_id):
        self._tour_repository.tour_delete_by_id(tour_id)
        self._tour_repository.write_data()

    def update_by_id(self, tour_id, name, description, price, duration, climat, tour_code):
        self._tour_repository.tour_replace_by_id(tour_id, name, description, price, duration, climat, tour_code)
        self._tour_repository.write_data()

    def add(self, tour):
        self._tour_repository.add_tour(tour)
        self._tour_repository.write_data()

    def get_count(self):
        return self._tour_repository.get_count()
