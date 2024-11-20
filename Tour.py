class Tour(BriefTour):
    def __init__(self, tour_id: int = 0, name: str = "", description: str = "", price: Decimal = Decimal(0), duration: int = 0, climat: str = ""):
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
        if not isinstance(value, int) or value < 0:
            raise ValueError("Duration must be a non-negative integer.")
        self._duration = value

    @property
    def climat(self):
        return self._climat

    @climat.setter
    def climat(self, value: str):
        if not isinstance(value, str) or not value:
            raise ValueError("climat must be a non-empty string.")
        self._climat = value


