class BriefTour:
    def __init__(self, tour_id: int = 0, name: str = "", price: int = 10):
        self.tour_id = tour_id
        self.name = name
        self.price = price

    @property
    def tour_id(self):
        return self._tour_id

    @tour_id.setter
    def tour_id(self, value: int):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Id must be a non-negative integer.")
        self._tour_id = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        if not isinstance(value, str): 
           raise ValueError("Name must contain at least one letter.")
        self._name = value

    @property
    def price(self):
        return self._tour_id

    @price.setter
    def price(self, value: int):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Price must be a non-negative integer.")
        self._price = value

    def __eq__(self, other):
        if not isinstance(other, BriefTour):
            return False
        return (self.name == other.name)

