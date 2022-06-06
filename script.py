import csv

filename='data.csv'

seed = ''

artists = []

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # for index, column_header in enumerate(header_row):
    #     print(index,column_header)

    for row in reader:

        artist = row[3].replace("'","''")
        commaIndex = artist.find(',')
        if commaIndex > 0:
            artist = f'{artist[commaIndex + 2:]} {artist[:commaIndex]}'
        
        artists.append(artist)

        # title = row[4].replace("'","''")
        # year = row[5]

        # rank_2003 = row[0]
        # rank_2012 = row[1]
        # rank_2020 = row[2]
        # if rank_2003 == '': rank_2003 = 0
        # if rank_2012 == '': rank_2012 = 0
        # if rank_2020 == '': rank_2020 = 0

        # image = f'http://alexdietz.com/covers/{rank_2020}.jpg'

        # seed += f'INSERT INTO main_app_album(title, artist, image, rank_2003, rank_2012, rank_2020, year)\n\tVALUES\n\t\t('
        # seed += f"'{title}', '{artist}', '{image}', {rank_2003}, {rank_2012}, {rank_2020}, {year});\n\n"

# text_file = open("seed.txt", "w")
# n = text_file.write(seed)
# text_file.close()