# Project: Study Program Organization Assistant

**Project Idea**
	•A tool to help students decide which courses to pick in the upcoming
	semester
	•Provides information about the courses and shows how the semester is
	shaping up
	
# Project Architecture and Components

├── index.html
├── main.js
├── AllData.json 
├── App.vue
├── components
│   ├── About.vue
│   ├── AddCourse.vue
│   ├── Conflicts.vue   *To get the conflicts in course time
│   ├── HomePage.vue
│   ├── HorizontalBarChart.vue   *To generate a bar chart
│   ├── PieChart.vue   *To generate a pie chart
│   ├── SemesterCourses.vue
│   ├── StackedBarChart.vue   *To generate a stacked bar chart
│   └── TimeTable.vue   *To generate the final timetable
└── README.md

The charts were generated using chart.js and vue-chartjs libraries.
To generate the final table, we have used vue-cal library, this library provides calendar table.

# Steps on running the project

* Download and extract this repository.

*Download and install YARN and Node.js

*Install the needed libraries

*To start a project you have to use the comand "yarn serve"