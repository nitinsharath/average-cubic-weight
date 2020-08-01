from typing import List

import requests

from models.product import Product


def get_products(filter_by_category=None) -> List[Product]:
    """
    Gets all products from the products endpoint.

    Sample format of the api:
    {
        "objects": [
            {
                "category": "Carpet & Steam Cleaners",
                "title": "Kogan 360\\u00b0 Magic Spin Mop",
                "weight": 2300,
                "size": {
                "width": 31,
                "length": 47,
                "height": 29
            },
            ...
            "next": "/api/products/3"
        ]

    },

    :param filter_by_category: If specified, will filter products by this category
    """
    products = []

    base_url = 'http://wp8m3he1wt.s3-website-ap-southeast-2.amazonaws.com'

    # This is a paginated endpoint, so we query until "next" is null
    # We initialise the next url with the first page
    next_url = '/api/products/1'

    while next_url:
        response = requests.get(base_url + next_url)
        response.raise_for_status()
        data = response.json()

        objects = data['objects']
        next_url = data['next']

        if filter_by_category:
            objects = filter(
                lambda o: o['category'] == filter_by_category,
                objects,
            )

        for obj in objects:
            category = obj['category']
            size = obj['size']
            if size:
                width = size['width']
                length = size['length']
                height = size['height']
            else:
                width, length, height = 0, 0, 0

            products.append(Product(
                category=category,
                width=width,
                length=length,
                height=height,
            ))

    return products
