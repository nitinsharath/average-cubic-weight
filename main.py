from models.product import Product
from services.get_products import get_products


def get_average_cubic_weight_of_air_conditioners() -> float:
    products = get_products(filter_by_category='Air Conditioners')
    return Product.get_average_cubic_weights(products=products)


if __name__ == '__main__':
    average_cubic_weight = get_average_cubic_weight_of_air_conditioners()
    print('The average cubic weight of Air conditioners is: ', average_cubic_weight, 'kg')
