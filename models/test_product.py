import unittest
from unittest import TestCase

from models.product import Product


class TestProduct(TestCase):
    def setUp(self) -> None:
        self.product_1 = Product(category='Cat 1', width=30, length=40, height=20)
        self.product_2 = Product(category='Cat 2', width=49.5, length=56.7, height=87.5)
        self.product_3 = Product(category='Cat 3', width=53.7, length=80, height=15.4)

    def test_get_cubic_weight(self):
        self.assertEqual(self.product_1.get_cubic_weight(), 6.0)
        self.assertEqual(self.product_2.get_cubic_weight(), 61.39546875)
        self.assertEqual(self.product_3.get_cubic_weight(), 16.5396)

    def test_get_average_cubic_weights(self):
        products = [self.product_1, self.product_2, self.product_3]
        self.assertEqual(Product.get_average_cubic_weights(products), 27.97835625)
