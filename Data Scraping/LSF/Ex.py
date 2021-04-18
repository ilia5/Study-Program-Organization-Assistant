from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

page_url = 'https://campus.uni-due.de/lsf/rds?state=verpublish&status=init&vmfile=no&publishid=327508&moduleCall=webInfo&publishConfFile=webInfo&publishSubDir=veranstaltung'

# opens the connection and downloads html page from url
uClient = uReq(page_url)

# parses html into a soup data structure to traverse html
# as if it were a json data type.
page_soup = soup(uClient.read(), "html.parser")
uClient.close()

# finds each product from the store page
containers = page_soup.findAll("form", {"class": "form"})
# name the output file to write to local disk
out_filename = "Course_time_room.csv"
headers = "Course, Day, Time, Room, Semester \n"

# opens file, and writes headers
f = open(out_filename, "w", encoding='utf8')
f.write(headers)
container = containers[0]
if( len(container.select("td"))>28):
    room = container.select("td")[19].text
    day = container.select("td")[15].text
    time = container.select("td")[16].text
    room = room.strip()
    day = day.strip()
    time = time.strip()
    f.write("Courrse" + ", " + day + ", " + time + ", " + room + ", " + "WS" + "\n")
    room = container.select("td")[30].text
    day = container.select("td")[26].text
    time = container.select("td")[27].text
    room = room.strip()
    day = day.strip()
    time = time.strip()
    f.write("Courrse" + ", " + day + ", " + time + ", " + room + ", " + "WS" + "\n")


else:
    room = container.select("td")[19].text
    day = container.select("td")[15].text
    time = container.select("td")[16].text
    room = room.strip()
    day = day.strip()
    time = time.strip()
    f.write("Courrse" + ", " + day + ", " + time + ", " + room + ", " + "WS" + "\n")
f.close()