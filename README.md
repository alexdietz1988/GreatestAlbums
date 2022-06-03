# Greatest Albums

## Project description
Greatest Albums is an app where users can explore Rolling Stone’s 2020 list of the [500 Greatest Albums of All Time](https://www.rollingstone.com/music/music-lists/best-albums-of-all-time-1062063/). Users will be able to sort albums by rank or date, filter albums by decade or year. They will also be able to mark albums as “want to listen,” “favorite,” or “listened,” and e.g. see just the albums they haven’t listened to.

The user interface design is inspired by the film website [Letterboxd](https://letterboxd.com). Another inspiration is [The Greatest Books](https://thegreatestbooks.org).

## User stories
1. I want to see what the site is about, and click on a link to register or login, which will take me to a register/login page.
2. I want to see a grid displaying covers for all the albums on the list.
3. Mousing over an album cover should tell me the album title, artist, and rank.
4. I want to be able to click on an album and see the album details, and choose whether to mark/unmark it as “want to listen”, “favorite,” or “listened”.
5. From the album detail page, I want to be able to click on the artist’s name and see a grid displaying covers for all that artist’s albums that appear on the list.
6. From the main album list view, I want to be able to use dropdown menus to select different sorting/filtering options, including sort by rank vs. sort by date; filter by decade or by year; and filter by what what I’ve marked as “want to listen,” “favorite,” or “listened.”
7. I should also be able to access grids of what I’ve marked as “want to listen” etc. through links on the header.

## Project plan
I plan to build the app entirely in Django. I’ll use [this spreadsheet](https://docs.google.com/spreadsheets/d/1QguM-JM3LAJuZlnmY8aN0MutBJrZAzDs3aWZWTtF1WU/edit#gid=0) to get the album details. I plan to look into using a Python script to automate the process of getting the album covers. If I can’t get this to work, I would manually get covers for e.g. just the top 50 albums.

- [ ] Album index (just a list of titles to start)
- [ ] Album detail
- [ ] Filter by decade
- [ ] Filter by year
- [ ] Convert album index to cover grid
- [ ] User accounts
- [ ] User data features ("want to read" etc.)
- [ ] Albums by artist
- [ ] (Stretch) Select multiple filters at once (e.g. albums from the 70s that I haven't listened to)
- [ ] (Stretch) Apply filters to albums by artist

## Wireframes
<img width="764" alt="Wireframes" src="https://user-images.githubusercontent.com/100381791/171869114-6e33597c-034b-4a28-a1e7-70d2800f55f6.png">

### Notes

- The three elements above the cover grid are dropdown menus.
- On index pages, mouseover an album cover to see album title, artist, and rank

## ERD
<img width="474" alt="ERD" src="https://user-images.githubusercontent.com/100381791/171869248-eb0f1831-11cb-46ce-b1c3-837d4f5fc135.png">