import os
import xml.etree.ElementTree as ET

os.system('cls')


tree = ET.parse('goods.xml')
root = tree.getroot()

sum = 0
for prod in root.findall('product'):
    price = prod.find('price').text if prod.find('price') is not None else '0'
    quantity = prod.find('qt').text if prod.find('qt') is not None else '0'
    money = int(price)
    number = int(quantity)
    sum += money * number
print(f'Summary price is {sum}')
