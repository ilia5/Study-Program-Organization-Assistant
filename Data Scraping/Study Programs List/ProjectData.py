from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

page_url = 'https://www.uni-due.de/vdb/studiengang/liste'

# opens the connection and downloads html page from url
uClient = uReq(page_url)

# parses html into a soup data structure to traverse html
# as if it were a json data type.
page_soup = soup(uClient.read(), "html.parser")
uClient.close()

studyProgramContainers = page_soup.findAll("div", {"class": "highlight-blue"})
# name the output file to write to local disk
out_filename = "Courses_data.csv"
# header of csv file to be written
headers = "Study Program, Courses, Professor, Semester, V, Ü, P, S, Credits \n"

# opens file, and writes headers
f = open(out_filename, "w")
f.write(headers)

allCourses = ['Angewandte Informatik','Angewandte Kognitions','Computer Engineering']

# loops over each product and grabs attributes about
# each product
studyProgramContainer = studyProgramContainers[0]
for studyProgram in studyProgramContainer.select("a"):
    checkInAllCourses = 0
    for oneCourse in allCourses:
        if(studyProgram.text.find("19") != -1):
            continue
        elif(studyProgram.text.find(oneCourse) != -1):
            checkInAllCourses = 1
            break
    if(checkInAllCourses == 1):
        page_url = 'https://www.uni-due.de' + studyProgram['href']

        # opens the connection and downloads html page from url
        uClient = uReq(page_url)

        # parses html into a soup data structure to traverse html
        # as if it were a json data type.
        page_soup = soup(uClient.read(), "html.parser")
        uClient.close()

        # finds each product from the store page
        containers = page_soup.findAll("fieldset", {"class": "highlight-yellow"})
        sem = 1
        for container in containers:
            semester = "Semester "+ str(sem)
            course = "0"
            vupsc = [0,0,0,0,0,0,0] 
            i = 9
            for courseInfo in container.select("a"):
                if(courseInfo.text.find("Dr.") != -1 or courseInfo.text.find("M.Sc.") != -1 ):
                    continue
                elif(courseInfo.text.find("Wahlpflicht") != -1 or courseInfo.text.find("Ergänzungsbereich") != -1 or courseInfo.text.find("Wahlpflichtkatalog") != -1 or courseInfo.text.find("Non-Technical") != -1 or courseInfo.text.find("Wahl") != -1 or
                 courseInfo.text.find("E1") != -1 or courseInfo.text.find("E2") != -1 or courseInfo.text.find("E3") != -1 or courseInfo.text.find("Elective") != -1 or courseInfo.text.find("Nicht-technischer") != -1 or courseInfo.text.find("M-AI") != -1):
                    if(course == "0"):
                        i = i + 7
                        continue
                    else:
                        for j in range(5):
                            vupsc[j] = container.select("td")[i+j].text
                        f.write(studyProgram.text.replace(",", "|") +", " +course.replace(",", "|") +", "+ "-" +", " +semester+ ", " + vupsc[0] +", " +vupsc[1] + ", " + vupsc[2] + ", " + vupsc[3] + ", " +vupsc[4] +"\n")
                        course = "0"
                        i = i + 14  
                elif(courseInfo.text.find("Prof.") != -1 ):
                    if(course == "0"):
                        continue
                    else:
                        for j in range(5):
                            vupsc[j] = container.select("td")[i+j].text
                        f.write(studyProgram.text.replace(",", "|") +", " +course.replace(",", "|") +", "+courseInfo.text +", " +semester+ ", " + vupsc[0] +", " +vupsc[1] + ", " + vupsc[2] + ", " + vupsc[3] + ", " +vupsc[4] +"\n")
                        course = "0"
                        i = i + 7
                elif(course == "0"):     
                    course = courseInfo.text
                else:
                    for j in range(5):
                        vupsc[j] = container.select("td")[i+j].text
                    f.write(studyProgram.text.replace(",", "|") +", " +course.replace(",", "|") +", "+ "-" +", " +semester+ ", " + vupsc[0] +", " +vupsc[1] + ", " + vupsc[2] + ", " + vupsc[3] + ", " +vupsc[4] +"\n")
                    course = courseInfo.text
                    i = i + 7
            if(course != "0"):
                    for j in range(5):
                        vupsc[j] = container.select("td")[i+j].text
                    f.write(studyProgram.text.replace(",", "|") +", " +course.replace(",", "|") +", "+ "-" +", " +semester+ ", " + vupsc[0] +", " +vupsc[1] + ", " + vupsc[2] + ", " + vupsc[3] + ", " +vupsc[4] +"\n")
            sem = sem+1

f.close()  # Close the file