import requests
import json
import collections
from PIL import Image
import requests
from io import BytesIO

from hack_test import runner


def extract_info(response_content, product_info):
    """
    This function extract the info from the request content
    """
    json_data = json.loads(response_content)
    # product_info = collections.defaultdict(list)

    for product in json_data:
        product_sku = product['sku']
        product_thumbnail = product['thumbnail_image_url']

        # for key, val in product.items():
        #     print(key, val)

        product_info[product_sku].append(product_thumbnail)


def main():
    headers = {
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) \
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36',
    }

    page_counter = 1
    info_dict = collections.defaultdict(list)

    while True:
        response = requests.get('https://www.wayfair.com/3dapi/models?page={}'.format(page_counter), headers=headers,\
            auth=('nctl144@gmail.com', '5ca9202c12dcc'))

        if not response.text or response.text == '"No product(s) found."':
            break

        extract_info(response.text, info_dict)
        page_counter += 1



    for key, val in info_dict.items():
        product_thumbnail = val[0]

        return_image = requests.get(product_thumbnail)

        # print the good content to the terminal
        runner(BytesIO(return_image.content))




if __name__ == "__main__":
    main()
