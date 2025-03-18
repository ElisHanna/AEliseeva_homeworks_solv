import os
import xml.etree.ElementTree as ET

os.system('cls')


tree = ET.parse('goods.xml')
root = tree.getroot()

sum = 0.0
for prod in root.findall('product'):
    price = prod.find('price')
    quantity = prod.find('qt')

    text_price = price.text if price is not None else False
    text_quantity = quantity.text if quantity is not None else False

    money = float(text_price) if text_price is not None else False
    number = int(text_quantity) if text_quantity is not None else False
    sum += money * number
print(f'Summary price is {sum}')
