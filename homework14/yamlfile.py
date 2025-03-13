import os
import yaml

os.system('cls')

books = [
    {'name':'Modicine', 'Author': 'Nikita Zhukov', 'year': 2018},
    {'name':'The lost world', 'Author': 'Arthur Konan Doyle', 'year': 1978},
    {'name':'The time machine', 'Author': 'Herbert Wells', 'year': 2003},
    {'name':'Footprints on me', 'Author': 'Eugen Grishovets', 'year': 2009},
]
with open("books.yaml", "w") as file:
    yaml.dump(books, file)

def reading(filename):
    with open(filename) as f:
        print(f.read())

reading('books.yaml')


to_record = {
    'name': input('Enter the books name '),
    'Author': input("Enter author's name "),
    'year': input('Enter the year')
    }
with open('books.yaml', 'a') as f:
    yaml.dump(to_record, f)

reading('books.yaml')