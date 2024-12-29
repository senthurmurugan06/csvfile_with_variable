import csv
csv_file_path ="/Users/senthurmurugan/Documents/pyth1/data.csv"
csv_data = []
with open(csv_file_path, mode='r', newline='', encoding='ISO-8859-1') as file:
        reader = csv.reader(file)
        for row in reader:
            csv_data.append(row)

print(csv_data)
