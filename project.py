class Project:
    def __init__(self, level, title, desc, mentor, tags, slack, url):
        self.level = level
        self.title = title
        self.desc = desc
        self.mentor = mentor
        self.tags = tags
        self.slack = slack
        self.url = url
    
hello = Project(
            "Beginner", 
            "Hello-BitOverflow",
            "Submit Hello-World programs in any language, it should print the string 'Hello BitOverflow' at the standard output",
            "Pritom Gogoi",
            [{"hello":"Hello-World"}, {"multi":"Multi-Language"}],
            "https://join.slack.com/t/hello-bitoverflow/shared_invite/enQtNTM3NTUyODU1MzE1LWM4ZmMzZmNmZjEzZGI0YTZmMjg4MGRmMWE0NDA2MTRiZWU5Zjc4ZWE0MmIyNTMwM2VhOTg5Y2M1OGNkNzAyMzQ",
            "https://github.com/bitoverflow-in/hello-bitoverflow")
        

snake = Project(
            "Beginner", 
            "Snake Oil Product Page",
            "co-ordinate with your mentors and colleagues to design a product page for selling the (very effective) snake oil. A design sample is given in project documentation",
            "Pritom Gogoi",
            [{"html":"HTML"}, {"css":"CSS"}, {"js":"JS"}, {"front":"frontend"}],
            "https://join.slack.com/t/snake-oil-productpage/shared_invite/enQtNTM3NDg0ODA4MzA5LWNkNDA0NGNmYTczNjJjYzFjMjA3NTcwYWQxZmY5Mjc2ZTFkNzZmODI5OTMyZTYzZTFjMmRiOTllNTcwMDA2MmI",
            "https://github.com/bitoverflow-in/snake-oil-product-page")

calc = Project(
            "Beginner", 
            "Calculator-All",
            "Write code in any language for a calculator that can perform the four basic operations of additions, subtraction, multiplication and division",
            "Pritom Gogoi",
            [{"console":"Console-App"}, {"multi":"Multi-Language"}],
            "https://join.slack.com/t/calculator-all/shared_invite/enQtNTQwMzA5ODk3NzgyLTU3ZDQ2ZTIwOWNjYmU4YWEwNGVmYjEwMWY1Mzg2ODRjMWZiMTE5NTk0M2Y3ZjdkMzc2NWRjMWVkNzE3MjJlZDM",
            "https://github.com/bitoverflow-in/calculator-all")

stan = Project(
            "Beginner", 
            "Stan Lee Tribute Page",
            "Work together and create a tribute page for the comic book legend Stan Lee. A design sample is given in project documentation",
            "Pritom Gogoi",
            [{"html":"HTML"}, {"css":"CSS"}, {"js":"JS"}, {"front":"frontend"}],
            "https://join.slack.com/t/stanlee-tributepage/shared_invite/enQtNTQwMzA2Nzc5Nzk4LTQzODAwNzZlNzNhMjJjMmEyNmNhYzY5N2I3NjE2NDkyNTM4YzViYmM1NmE2YTQ3N2VhODZiZjE3NTE1ZDIwNDc",
            "https://github.com/bitoverflow-in/stan-lee-tribute-page")

scrape = Project(
            "Mainstream", 
            "Scrape-Site-Face",
            "Write a script that scrapes a given website url for images, once gathered search the images for face using any face detection algorithm and crop the faces as separate image files",
            "Pritom Gogoi",
            [{"py":"Python"}, {"scrape":"Web Scraping"}, {"cv":"OpenCV"}, {"auto":"Automating"}],
            "https://join.slack.com/t/scrape-site-face/shared_invite/enQtNTQwNzczNDc4NjQ1LWM2ZjRlZGEwMjQzMmMwYzg1NTA0ZDU2MmQxMmE0ZDhmMDczY2U0OTliMDczNjcyZmU4MzNmYmQyNTBiMDdmMGY",
            "https://github.com/bitoverflow-in/scrape-site-face")

youtubemp3 = Project(
            "Mainstream", 
            "Youtube-MP3-GUI",
            "Design a GUI for a youtube to mp3 converter script. The script is written using python and the GUI is to be developed using tkinter GUI library. ",
            "Pritom Gogoi",
            [{"py":"Python"}, {"gui":"GUI"}, {"tk":"Tkinter"}, {"yt":"Youtube-DL"}],
            "https://join.slack.com/t/youtube-mp3-gui/shared_invite/enQtNTQxOTEwNzYzNDc5LWZiNGVjOTc5N2ZiNDJjZmI1NWE5OGYwNWZkYzM0Mzc1ZmM0NmYyY2RlMzRlYmZjNjgxZWRmMTZmMjA1OGFjYWU",
            "https://github.com/bitoverflow-in/youtube-mp3-gui")

learntk = Project(
            "Beginner", 
            "Learn Tkinter",
            "Learn the Basics of making GUI using tkinter and implement it in making designs for On-screen Keyboard and TV Remote",
            "Pritom Gogoi",
            [{"py":"Python"}, {"gui":"GUI"}, {"tk":"Tkinter"}],
            "https://join.slack.com/t/learn-tkinter/shared_invite/enQtNTQwMjQ1NjMyMTI5LWI1ZmNkZTAwZjZmZjlkZmJhNWI0OGM5NGE1NmJhMDhkNzBjNjVkMTUyMzVhMWUwZGNmMjQ1MGJmYWQ2ZDhmMjY",
            "https://github.com/bitoverflow-in/learn-tkinter")

subwar = Project(
            "Mainstream", 
            "Pewdiepie-V-Tseries",
            "Create a webpage showing live subcriber count for the ongoing subcriber war between the King of Youtube, PewDiePie and Corporate Giant, T-Series. Be a part of this battle and maintain the record of daily subcriber count.",
            "Pritom Gogoi",
            [{"yt":"Youtube"}, {"api":"API"}, {"front":"frontend"}],
            "https://join.slack.com/t/stanlee-tributepage/shared_invite/enQtNTQwMzA2Nzc5Nzk4LTQzODAwNzZlNzNhMjJjMmEyNmNhYzY5N2I3NjE2NDkyNTM4YzViYmM1NmE2YTQ3N2VhODZiZjE3NTE1ZDIwNDc",
            "https://github.com/bitoverflow-in/pewdiepie-v-tseries")

imgur = Project(
            "Mainstream", 
            "UrPhoto",
            "Ever heard of Imgur, online image sharing community and image host; Here is your chance to build your own version of Imgur with your custom Tech Stack",
            "Rajat Kanti Bhattacharjee",
            [{"node":"NodeJS"}, {"js":"Javascript"}, {"exp":"Express"}, {"mgdb":"MongoDB"}],
            "https://join.slack.com/t/stanlee-tributepage/shared_invite/enQtNTQwMzA2Nzc5Nzk4LTQzODAwNzZlNzNhMjJjMmEyNmNhYzY5N2I3NjE2NDkyNTM4YzViYmM1NmE2YTQ3N2VhODZiZjE3NTE1ZDIwNDc",
            "https://github.com/bitoverflow-in/urphoto")


projectList = [hello, scrape, snake, imgur, calc, stan, subwar, learntk, youtubemp3, ]