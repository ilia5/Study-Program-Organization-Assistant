import csv
import urllib
import unicodedata
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

courseList=[]
csv_file = open('Courses_List.txt') 
csv_reader = csv.reader(csv_file, delimiter=',')
for row in csv_reader:
    courseList.append(row[0])
csv_file.close()
out_filename = "Course_time_room.csv"
headers = "Course, Day, Time, Room, Semester, Link \n"
f = open(out_filename, "w")
f.write(headers)
for courseName in courseList:
    print(courseName)
    page_urlWS = 'https://campus.uni-due.de/lsf/rds?state=wsearchv&search=1&subdir=veranstaltung&veranstaltung.dtxt='+urllib.parse.quote(courseName) +'&veranstaltung.semester=20192&P_start=0&P_anzahl=10&P.sort=&_form=display'
    page_urlSS = 'https://campus.uni-due.de/lsf/rds?state=wsearchv&search=1&subdir=veranstaltung&veranstaltung.dtxt='+urllib.parse.quote(courseName) +'&veranstaltung.semester=20191&P_start=0&P_anzahl=10&P.sort=&_form=display'

    uClient = uReq(page_urlWS)


    page_soup = soup(uClient.read(), "html.parser")
    uClient.close()

    containersWS = page_soup.findAll("div", {"class": "divcontent"})

    containerWS = containersWS[0]

    uClient = uReq(page_urlSS)


    page_soup = soup(uClient.read(), "html.parser")
    uClient.close()

    containersSS = page_soup.findAll("div", {"class": "divcontent"})

    containerSS = containersSS[0]
    if(len( containerSS.select("tr")) > 1):
        index = 0
        page_url = '0'
        for row in containerSS.select("tr"):
            if(index == 0):
                index = 1
                continue
            if(row.select("td")[2].text.find("Seminar") != -1 or row.select("td")[2].text.find("Praktikum") != -1 or row.select("td")[1].text.find("E1") != -1 or row.select("td")[1].text.find("E2") != -1 or row.select("td")[1].text.find("E3") != -1):
                continue
            elif(row.select("td")[2].text.find("Klausur") != -1 or row.select("td")[2].text.find("Übung") != -1 or row.select('td')[2].text.find("Vorlesung") != -1 ):
                 page_url = row.select("td")[1].find('a').get('href')
                 break

        if(page_url != '0'):
            # opens the connection and downloads html page from url
            uClient = uReq(page_url)

            # parses html into a soup data structure to traverse html
            # as if it were a json data type.
            page_soup = soup(uClient.read(), "html.parser")
            uClient.close()

            # finds each product from the store page
            containers = page_soup.findAll("form", {"class": "form"})
            container = containers[0]
            if(len(container.select("td")) > 19):
                print("SS")
                room = container.select("td")[19].text
                day = container.select("td")[15].text
                time = container.select("td")[16].text
                room = room.strip()
                day = day.strip()
                time = time.strip()
                f.write(courseName + ", " + day + ", " + time + ", " + room + ", " + "SS, " + page_url + "\n")

    if(len( containerWS.select("tr")) > 1):
        index = 0
        page_url = '0'
        for row in containerWS.select("tr"):
            if(index == 0):
                index = 1
                continue
            if(row.select("td")[2].text.find("Praktikum") != -1 or row.select("td")[1].text.find("E1") != -1 or row.select("td")[1].text.find("E2") != -1 or row.select("td")[1].text.find("E3") != -1):
                continue
            elif(row.select("td")[2].text.find("Klausur") != -1 or row.select("td")[2].text.find("Übung") != -1 or row.select('td')[2].text.find("Vorlesung") != -1 or row.select("td")[2].text.find("Seminar") != -1 ):
                 page_url = row.select("td")[1].find('a').get('href')
                 break

        if(page_url != '0'):
            # opens the connection and downloads html page from url
            uClient = uReq(page_url)

            # parses html into a soup data structure to traverse html
            # as if it were a json data type.
            page_soup = soup(uClient.read(), "html.parser")
            uClient.close()

            # finds each product from the store page
            containers = page_soup.findAll("form", {"class": "form"})
            container = containers[0]
            if(len(container.select("td")) > 19):
                print("WS")
                room = container.select("td")[19].text
                day = container.select("td")[15].text
                time = container.select("td")[16].text
                room = room.strip()
                day = day.strip()
                time = time.strip()
                if(courseName == 'Marketing' or courseName == 'Technische Mechanik 1' ):
                    room = 'S04 T01 A01'
                f.write(courseName.replace("+"," ")+ ", " + day + ", " + time + ", " + room+ ", " + "WS, " + page_url +"\n")
f.close()