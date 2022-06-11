# Greatest Albums

## About
Greatest Albums is an app where users can explore *Rolling Stone*’s [2020 list](https://www.rollingstone.com/music/music-lists/best-albums-of-all-time-1062063/) of the 500 Greatest Albums of All Time. You can check out the app [here](https://greatestalbums.herokuapp.com).

As a user, you can browse all albums; see album details, including other albums by the artist featured on the RS list; and save an album to your "favorites," "want to listen," "listened," or "not interested" list. You can also filter albums by decade or year, or see only albums that you haven't yet added to your lists.

**Technologies Used**: Django, PostgreSQL, Heroku, AWS

The user interface design is inspired by [Letterboxd](https://letterboxd.com) and [Musicboard](https://musicboard.app). Another inspiration is [The Greatest Books](https://thegreatestbooks.org).

## Screenshots
![image](screenshots/all_albums.png)
![image](screenshots/album_detail.png)

## Getting Started / Contribution Guidelines
You can use the app by clicking [here](https://greatestalbums.herokuapp.com).

If you'd like to contribute to the app, you can fork and clone this repo, make changes, and submit a pull request. If you notice a bug or want to propose an idea for improving the app, you can submit it as an issue to this repo.

## User Stories
1. I want to see what the site is about, and click on a link to register or login, which will take me to a register/login page.
2. I want to see a grid displaying covers for all the albums on the list.
3. Mousing over an album cover should tell me the album title, artist, and rank.
4. I want to be able to click on an album and see the album details, and choose whether to mark/unmark it as “want to listen”, “favorite,” or “listened”.
5. From the album detail page, I want to be able to click on the artist’s name and see a grid displaying covers for all that artist’s albums that appear on the list.
6. From the main album list view, I want to be able to use dropdown menus to select different sorting/filtering options, including sort by rank vs. sort by date; filter by decade or by year; and filter by what what I’ve marked as “want to listen,” “favorite,” or “listened.”
7. I should also be able to access grids of what I’ve marked as “want to listen” etc. through links on the header.

## Wireframes
![image](screenshots/wireframes.png)

## ERD
![image](screenshots/erd.png)

## Development Roadmap
- [x] Album index, album detail
- [x] Filter album index by decade, year
- [x] User accounts; add album to my lists
- [x] Album detail: Other albums by artist
- [x] Filter out albums in user lists
- [ ] "Comfy" view in album index
- [ ] Switch to rankings from RS's 2003 or 2012 list
- [ ] Sort albums by date
- [ ] Search albums by title/artist
- [ ] Organize CSS with Sass
- [ ] Signup/login with Google/Apple/Facebook