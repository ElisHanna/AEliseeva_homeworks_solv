import os
import xml.etree.ElementTree as ET

os.system('cls')


tree = ET.parse('goods.xml')
root = tree.getroot()

sum = 0
for prod in root.findall('product'):
    price = prod.find('price').text
    quantity = prod.find('qt').text
    sum += int(price)*int(quantity)
print(f'Summary price is {sum}')
