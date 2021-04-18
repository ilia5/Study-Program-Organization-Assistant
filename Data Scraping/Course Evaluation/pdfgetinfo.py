import PyPDF2
import csv
import unicodedata

# In order to get the data from the PDF files, you have to download them first and add courses names to the text file 'course_list.txt'
courseList=[]
csv_file = open('course_list.txt') 
csv_reader = csv.reader(csv_file, delimiter=',')
for row in csv_reader:
    courseList.append(row[0])
csv_file.close()
out_filename = "Course_time_room.csv"
headers = "Courses ,Difficulty, Usefulness for work, Study outside course,  Realistic expectation, Scripts, Pace \n"
f = open(out_filename, "w")
f.write(headers)
searchWords = ['10. Schwierigkeitsgr','15. Theorie_Praxis_Bezug','27. Aufwand_Vor_Nachbereitung','16. Anforderungen_realisierbar','11. Hilfsmittel','13. Tempo']

searchWords2 = ['11. Schwierigkeitsgrad','15. Theorie_Praxis_Bezug','18. Workload','19. Aufwand leistbar','25. Hilfsmittel','9. Tempo']
for course in courseList:    
    pdfFileObj = open(course + '.pdf', 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    pageNumber = pdfReader.numPages
    index = 0
    mittelwert = ['0'] * 6
    for word,word2 in zip(searchWords,searchWords2):
        for i in range(2,pageNumber):
            pageObj = pdfReader.getPage(i)
            str = pageObj.extractText()
            if(str.find(word) != -1):
                ind = str.find('Mittelwert', str.find(word))
                newstr = str[ind +12] + str[ind +13]+ str[ind +14] + str[ind +15] + str[ind +16]
                print(course +"  :" +word +"  :" + newstr)
                mittelwert[index] = newstr
                break
            elif(str.find(word2) != -1):
                ind = str.find('Mittelwert', str.find(word2))
                newstr = str[ind +12] + str[ind +13]+ str[ind +14] + str[ind +15] + str[ind +16]
                print(course +"  :" +word2 +"  :" + newstr)
                mittelwert[index] = newstr                
        index  = index + 1
    f.write(course+ "," + mittelwert[0].replace(",",".").replace('\n', '') + "," + mittelwert[1].replace(",",".").replace('\n', '')  + "," +mittelwert[2].replace(",",".").replace('\n', '')  + "," + mittelwert[3].replace(",",".").replace('\n', '')  +"," + mittelwert[4].replace(",",".").replace('\n', '')  +","+ mittelwert[4].replace(",",".").replace('\n', '') +"\n")

