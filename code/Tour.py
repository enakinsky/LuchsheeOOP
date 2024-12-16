# -*- coding: cp1251 -*-
import json
import yaml
from BriefTour import BriefTour

class Tour(BriefTour):
    def __init__(self, tour_id: int = 0, name: str = "", description: str = "", price: int = 0,
                 duration: int = 0, climat: str = "", tour_code: str = ""):
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
    def create_new_tour(cls, name: str, description: str, price: int, duration: int, climat: str, tour_code: str):
        return cls(name=name, description=description, price=price, duration=duration, climat=climat, tour_code=tour_code)

    @classmethod
    def update_existing_tour(cls, tour_id: int, name: str, description: str, price: int, duration: int,
                             climat: str, tour_code: str):
        return cls(tour_id=tour_id, name=name, description=description, price=price, duration=duration, climat=climat, tour_code=tour_code)

    @classmethod
    def create_from_string(cls, tour_string: str):
        parts = tour_string.split(",")
        if len(parts) != 7:
            raise ValueError("Invalid tour string format. Expected 7 comma-separated values.")
        try:
            return cls(
                tour_id=int(parts[0].strip()),
                name=parts[1].strip(),
                description=parts[2].strip(),
                price=int(parts[3].strip()),
                duration=int(parts[4].strip()),
                climat=parts[5].strip(),
                tour_code=parts[5].strip()
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
            price=data['price'],
            duration=data['duration'],
            climat=data['climat'],
            tour_code=data['tour_code']
        )

    @classmethod
    def create_from_dict(cls, data: dict):
        return cls(
            tour_id=data.get('tour_id'),
            name=data['name'],
            description=data['description'],
            price=data['price'],
            duration=data['stock_quantity'],
            climat=data['material'],
            tour_code=data['tour_code']
        )

    def to_json(self) -> str:
        return json.dumps({
            'tour_id': self.tour_id,
            'name': self.name,
            'description': self.description,
            'price': str(self.price),
            'duration': self.duration,
            'climat': self.climat,
            'tour_code': self.tour_code
        }, ensure_ascii=False)

     @classmethod
    def create_from_yaml(cls, yaml_string: str):
        data = yaml.safe_load(yaml_string)
        return cls(
            tour_id=data.get('tour_id'),
            name=data['name'],
            description=data['description'],
            price=data['price'],
            duration=data['duration'],
            climat=data['climat'],
            tour_code=data['tour_code']
        )

    def to_yaml(self) -> str:
        return yaml.dump({
            'tour_id': self.tour_id,
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'duration': self.duration,
            'climat': self.climat,
            'tour_code': self.tour_code
        }, allow_unicode=True)

    def to_dict(self) -> dict:
        return {
            "tour_id": self.tour_id,
            "name": self.name,
            "description": self.description,
            "price": self.price,  
            "duration": self.duration,
            "climat": self.climat,
            "tour_code": self.tour_code
        }

    def __str__(self):
        return f"tour(tourId={self.tour_id}, name='{self.name}', description='{self.description}', price={self.price}, duration={self.duration}, climat='{self.climat}', tourCode='{self.tour_code}')"
