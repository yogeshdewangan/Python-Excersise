import random


def run(product, firmware, feature):
    rand_int = random.randint(0, 1)
    test_result = False
    if rand_int == 0:
        test_result = True

    print(f'product: {product}, firmware: {firmware}, feature: {feature} Test Result: {test_result}')
    return test_result


def test():
    products = ['p1', 'p2', 'p3']
    firmwares = ['f1', 'f2', 'f3']
    features = ['fe1', 'fe2', 'fe3']

    products_result = {'p1': 0, 'p2': 0, 'p3': 0}
    firmware_result = {'f1': 0, 'f2': 0, 'f3': 0}
    feature_result = {'fe1': 0, 'fe2': 0, 'fe3': 0}

    for product in products:
        for firmware in firmwares:
            for feature in features:
                result = run(product, firmware, feature)
                if result == False:
                    products_result[product] += 1
                    firmware_result[firmware] += 1
                    feature_result[feature] += 1

    return products_result, firmware_result, feature_result


products_result, firmware_result, feature_result = test()
print(products_result, firmware_result, feature_result)

def report(products_result, firmware_result, feature_result):
    product_max_failure = max(zip(products_result.values(), products_result.keys()))[1]
    firmware_max_failure = max(zip(firmware_result.values(), firmware_result.keys()))[1]
    feature_max_failure = max(zip(feature_result.values(), feature_result.keys()))[1]

    print(f'product {product_max_failure} has maximum failures {products_result[product_max_failure]}')
    print(f'firmware {firmware_max_failure} has maximum failures {firmware_result[firmware_max_failure]}')
    print(f'feature {product_max_failure} has maximum failures {feature_result[feature_max_failure]}')

report(products_result, firmware_result, feature_result)