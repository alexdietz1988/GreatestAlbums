import csv

filename='data.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for index, column_header in enumerate(header_row):
        print(index,column_header)

    artists, titles = [], []
    for row in reader:

        artist = row[3]
        commaIndex = artist.find(',')
        if commaIndex > 0:
            artist = f'{artist[commaIndex + 2:]} {artist[:commaIndex]}'
        artists.append(artist)

        title = row[4]
        titles.append(title)

print(artists)
print(titles)