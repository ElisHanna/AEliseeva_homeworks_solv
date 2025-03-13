import os
import xml.etree.ElementTree as ET

os.system('cls')


tree = ET.parse('goods.xml')
root = tree.getroot()

sum = 0.0
for prod in root.findall('product'):
    price = prod.find('price')
    quantity = prod.find('qt')

    text_price = price.text if prod.find('qt') is not None else '0'
    text_quantity = quantity.text if prod.find('qt') is not None else '0'

    money = float(text_price) if text_price is not None else False
    number = int(text_quantity) if text_quantity is not None else False
    sum += money * number
print(f'Summary price is {sum}')
