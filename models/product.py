from statistics import mean
from typing import List


class Product:
    CUBIC_WEIGHT_CONVERSION_FACTOR = 250  # Factor to convert cubic volume to weight

    def __init__(self, category: str, width: float, length: float, height: float):
        """ The width, length and height are assumed to be in cm """
        self.category = category
        self.width = width
        self.length = length
        self.height = height

    def get_cubic_weight(self) -> float:
        """ Returns cubic weight in kg """
        return self._get_cubic_volume() * self.CUBIC_WEIGHT_CONVERSION_FACTOR

    def _get_cubic_volume(self) -> float:
        """ Returns cubic volume in m3 """
        return self.width * self.length * self.height / 1000000

    @staticmethod
    def get_average_cubic_weights(products: List['Product']):
        cubic_weights = [p.get_cubic_weight() for p in products]
        return mean(cubic_weights)

