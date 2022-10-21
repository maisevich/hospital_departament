import csv


def add_file(data):
    with open('personal.txt', 'a', encoding='utf-8') as File:
        writer = csv.writer(File)
        writer.writerow(data)


def show_list_employees():
    with open('personal.txt', encoding='utf-8') as File:
        reader = csv.reader(File, delimiter=',', quotechar=',',
                            quoting=csv.QUOTE_MINIMAL)
        for row in reader:
            print(row)
