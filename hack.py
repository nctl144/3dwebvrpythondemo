import requests
import json
import collections

from hack_test import runner


def extract_info(request_content):
    """
    This function extract the info from the request content
    """

    json_data = json.loads(request_content)
    product_info = collections.defaultdict(list)

    for product in json_data:
        product_sku = product['sku']
        product_thumbnail = product['thumbnail_image_url']

        # for key, val in product.items():
        #     print(key, val)

        product_info[product_sku].append(product_thumbnail)

    return product_info

def main():
    headers = {
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) \
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36',
    }

    response = requests.get('https://www.wayfair.com/3dapi/models', headers=headers,\
        auth=('nctl144@gmail.com', '5ca9202c12dcc'))

    info_dict = extract_info(response.text)

    for key, val in info_dict.items():
        product_thumbnail = val[0]

        runner(product_thumbnail)




if __name__ == "__main__":
    main()
