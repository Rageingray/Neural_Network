import csv

csv_file_path = os.path.join(desktop_path, r"C:\Users\arshb\Desktop\diabetes.csv")

data = []
with open(csv_file_path, "r") as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        data.append(row)

column_widths = [max(len(str(item)) for item in col) for col in zip(*data)]

for i, header in enumerate(data[0]):
    print(header.ljust(column_widths[i]), end=" | ")
print()

for width in column_widths:
    print("-" * width, end=" | ")
print()

for row in data[1:]:
    for i, item in enumerate(row):
        print(str(item).ljust(column_widths[i]), end=" | ")
    print()
