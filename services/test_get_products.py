import json
from unittest import TestCase

import responses

from services.get_products import get_products


class TestGetProducts(TestCase):

    @responses.activate
    def test_get_products(self):
        base_url = 'http://wp8m3he1wt.s3-website-ap-southeast-2.amazonaws.com'
        response_data = {
            "objects": [
                {
                    "category": "Gadgets",
                    "title": "10 Pack Family Car Sticker Decals",
                    "weight": 120,
                    "size": {
                        "width": 15,
                        "length": 13,
                        "height": 1
                    }
                },
                {
                    "category": "Air Conditioners",
                    "title": "Window Seal for Portable Air Conditioner Outlets",
                    "weight": 235,
                    "size": {
                        "width": 26,
                        "length": 26,
                        "height": 5
                    }
                }
            ],
            "next": '/api/products/d',
        }
        responses.add(
            method=responses.GET,
            url=base_url + '/api/products/1',
            content_type='application/json',
            body=json.dumps(response_data),
            status=200,
        )

        response_data = {
            "objects": [
                {
                    "category": "Cables & Adapters",
                    "title": "3 Pack Apple MFI Certified Lightning to USB Cable (3m)",
                    "weight": 90.0,
                    "size": {
                        "width": 10.0,
                        "length": 20.0,
                        "height": 3.0
                    }
                },
                {
                    "category": "Air Conditioners",
                    "title": "Kogan 10,000 BTU Portable Air Conditioner (2.9KW)",
                    "weight": 26200.0,
                    "size": {
                        "width": 49.6,
                        "length": 38.7,
                        "height": 89.0
                    }
                }
            ],
            "next": None,
        }
        responses.add(
            method=responses.GET,
            url=base_url + '/api/products/d',
            content_type='application/json',
            body=json.dumps(response_data),
            status=200,
        )

        products = get_products()
        self.assertEqual(len(products), 4)

        self.assertEqual(products[0].category, 'Gadgets')
        self.assertEqual(products[0].width, 15)
        self.assertEqual(products[0].length, 13)
        self.assertEqual(products[0].height, 1)

        self.assertEqual(products[1].category, 'Air Conditioners')
        self.assertEqual(products[1].width, 26)
        self.assertEqual(products[1].length, 26)
        self.assertEqual(products[1].height, 5)

        self.assertEqual(products[2].category, 'Cables & Adapters')
        self.assertEqual(products[2].width, 10.0)
        self.assertEqual(products[2].length, 20.0)
        self.assertEqual(products[2].height, 3.0)

        self.assertEqual(products[3].category, 'Air Conditioners')
        self.assertEqual(products[3].width, 49.6)
        self.assertEqual(products[3].length, 38.7)
        self.assertEqual(products[3].height, 89.0)
