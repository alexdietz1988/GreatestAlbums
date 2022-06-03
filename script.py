import csv

filename = 'data.csv'

def format_artist(string):
    commaIndex = string.find(',')
    if commaIndex > 0:
        return f'{string[commaIndex + 2:]} {string[:commaIndex]}'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for index, column_header in enumerate(header_row):
        print(index, column_header)

    string = ''

    for row in reader:
        title = row[4]
        artist = format_artist(row[3])
        image =
        year = row[5]
        rank = row[2]

        string += f'INSERT INTO main_app_album(title, artist, image, rank, year) VALUES("{title}", "{artist}", {year}, {rank});'

    print(string)
