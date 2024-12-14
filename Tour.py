# --*-- encoding: cp1251 --*--
import json
from datetime import date
import re


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


class Tour(BriefTour):
    def __init__(self, tour_id: int = 0, name: str = "", description: str = "", price: int = 0,
                 duration: int = 0, climat: str = ""):
        super().__init__(tour_id, name, price)
        self.description = description
        self.duration = duration
        self.climat = climat

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value: str):
        if not isinstance(value, str) or not value:
            raise ValueError("Description must be a non-empty string.")
        self._description = value

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value: int):
        if not isinstance(value, int) or value < 1:
            raise ValueError("Duration must be a non-negative integer and not 0.")
        self._duration = value

    @property
    def climat(self):
        return self._climat

    @climat.setter
    def climat(self, value: str):
        if not isinstance(value, str) or not value:
            raise ValueError("climat must be a non-empty string.")
        self._climat = value

    @classmethod
    def create_new_tour(cls, name: str, description: str, price: int, duration: int, climat: str):
        return cls(name=name, description=description, price=price, duration=duration, climat=climat)

    @classmethod
    def update_existing_tour(cls, tour_id: int, name: str, description: str, price: int, duration: int,
                             climat: str):
        return cls(tour_id=tour_id, name=name, description=description, price=price, duration=duration, climat=climat)

    @classmethod
    def create_from_string(cls, tour_string: str):
        parts = tour_string.split(",")
        if len(parts) != 6:
            raise ValueError("Invalid tour string format. Expected 6 comma-separated values.")
        try:
            return cls(
                tour_id=int(parts[0].strip()),
                name=parts[1].strip(),
                description=parts[2].strip(),
                price=int(parts[3].strip()),
                duration=int(parts[4].strip()),
                climat=parts[5].strip()
            )
        except ValueError as e:
            raise ValueError("Invalid number format in tour string.") from e

    @classmethod
    def create_from_json(cls, json_string: str):
        data = json.loads(json_string)
        return cls(
            tour_id=data['tour_id'],
            name=data['name'],
            description=data['description'],
            price=int(data['price']),
            duration=data['duration'],
            climat=data['climat']
        )

    def to_json(self) -> str:
        return json.dumps({
            'tour_id': self.tour_id,
            'name': self.name,
            'description': self.description,
            'price': str(self.price),
            'duration': self.duration,
            'climat': self.climat
        }, ensure_ascii=False)

    def __str__(self):
        return f"tour(tourId={self.tour_id}, name='{self.name}', description='{self.description}', price={self.price}, duration={self.duration}, climat='{self.climat}')"


if __name__ == "__main__":
    try:
        tour1 = Tour.create_new_tour(
            name="Золотое кольцо Абхазии",
            description="Однодневная экскурсия по всем достопримечательностям",
            price=2000,
            duration=5,
            climat="Субтропики"
        )
        tour1.name = "qwe1"
        print(tour1)

    except ValueError as e:
        print("Error:", e)
