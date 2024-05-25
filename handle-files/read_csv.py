import csv
import json

#CSV methode
def read_csv(filename):
    with open(filename, encoding="UTF-8") as file:
        return csv.reader(file, delimiter=';')

def write_csv(filename, rows):
    with open(filename, "w") as file:
        writter = csv.writer(file,  delimiter = ";")
        writter.writerows(rows)


#TEXT methode
def read_text(filename):
    with open(filename, encoding='UTF-8') as file:
        return file.readlines()
    
for line in read_text(filename):
    print(line)


#JSON methode
def read_json(filename):
    with open(filename, encoding='UTF-8') as file:
        return json.load(file)

def write_json(filename, an_object):
    with open(filename, 'w', encoding='UTF-8') as file:
        json.dump(an_object, file, ensure_ascii=False, indent=2)
