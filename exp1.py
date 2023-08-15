data = []
with open('diabetes.csv', 'r') as file:
    lines = file.readlines()
    for line in lines[0:500]: 
        row = line.strip().split(',')
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
