# Project: Study Program Organization Assistant

**Project Idea**

	• A tool to help students decide which courses to pick in the upcoming semester
	• Provides information about the courses and shows how the semester is shaping up
	
# Project Architecture and Components
### Components:
The tool was created by using HTML/CSS/JS with the vue.js framework.

├── index.html\
├── main.js\
├── AllData.json\
├── App.vue\
├── components\
│   ├── About.vue\
│   ├── AddCourse.vue\
│   ├── Conflicts.vue   *To get the conflicts in course time\
│   ├── HomePage.vue\
│   ├── HorizontalBarChart.vue   *To generate a bar chart\
│   ├── PieChart.vue   *To generate a pie chart\
│   ├── SemesterCourses.vue\
│   ├── StackedBarChart.vue   *To generate a stacked bar chart\
│   └── TimeTable.vue   *To generate the final timetable\
└── README.md

* The charts were generated using chart.js and vue-chartjs libraries.
* To generate the final table, we have used vue-cal library, this library provides calendar table.
* It is a web application that was built using javascript without a backend.
* All data that we used in the project comes from the file AllData.json that is bundled with the website.

# The visualizations
### The amount of time that spent in different courses:

![image](https://user-images.githubusercontent.com/50524579/90310431-85b5f300-def1-11ea-9430-b0e978f90917.PNG)

### Total study time:

![image](https://user-images.githubusercontent.com/50524579/90310368-38d21c80-def1-11ea-83a5-11d3059795cb.PNG)

### The progress of the entire study program:

![image](https://user-images.githubusercontent.com/50524579/90310433-864e8980-def1-11ea-805c-8d4e8f6bc80b.PNG)

### The different aspects of courses:

![image](https://user-images.githubusercontent.com/50524579/90310430-851d5c80-def1-11ea-97db-5b9b250cfb3c.PNG)

### Final timetable:

![image](https://user-images.githubusercontent.com/50524579/90310432-85b5f300-def1-11ea-9e6d-94882f1bad2f.PNG)

# Steps on running the project

* Download and install YARN and Node.js
* Clone or download and extract this repository.
* Install the needed libraries by running this command 
```yarn``` 
* To run the project locally for development, run this command
```yarn serve```
* To build the project for deployment, run this command
```yarn build```
* After building the project you will get the website in "dist" folder
* You can upload the files into static filehosting service
* [Deployed version](https://ilia5.github.io/)

# Supervised by

* Professor dr. Mohamed Amine Chatti
* Dr. Arham Muslim
* Mouadh Guesmi

# Creators 

* Ilia Nassif
* Deniz Glawenda
