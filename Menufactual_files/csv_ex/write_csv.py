lunch = {
    '고갯마루': '02-123-4567',
    '세븐브렉스': '02-456-3573',
    '아랑졸돈까스': '02-6233-1232'
}

# 1. string formatting
# with open('lunch.csv', 'w', encoding = 'utf-8') as f:
#     for item in lunch.items():
#         f.write(f'{item[0]}, {item[1]}\n')

# 2. join
# with open('lunch.csv', 'w', encoding = 'utf-8') as f:
#     for item in lunch.items():
#         f.write(','.join(item) + '\n')

# 3. csv.writer
import csv
with open('lunch.csv', 'w', encoding = 'utf-8') as f:
    csv.writer = csv.writer(f)
    for item in lunch.items():
        csv.writer.writerow(item)
