<template>
  <div style="padding-bottom: 2rem">
    <h1>Here is your time table</h1>
    <div style="display: flex; flex-direction: column; grid-gap: 2rem">
      <div>
        <vue-cal
          selected-date="2018-11-19"
          active-view="week"
          :disable-views="['years', 'year', 'month', 'day']"
          hide-weekends
          hideTitleBar
          :timeFrom="8 * 60"
          :timeTo="20 * 60"
          hideViewSelector
          :events="events"
        />
        <p
          style="border: solid 1px #999; padding: 1rem 2rem;"
          v-for="course in coursesWithoutTime"
          :key="course"
        >
          {{ course.Courses }}
        </p>
        <conflicts :selected-courses="selectedCourses" />
      </div>
      <div style="display: flex; grid-gap: 2rem">
        <div style="flex: 1">
          <h2 style="text-align: center">Total Credits</h2>
          <horizontal-bar-chart
            :chartdata="barChartData"
            :options="barOptions"
          />
        </div>
        <div style="flex: 1">
          <h2 style="text-align: center">Course Evaluation</h2>
          <horizontal-bar-chart
            :chartdata="bar2ChartData"
            :options="bar2Options"
          />
          <p style="text-align: center">
            Values work like a grade system (lower = better)
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import VueCal from "vue-cal";
import "vue-cal/dist/vuecal.css";
import CourseData from "../AllData.json";
import Conflicts from "./Conflicts.vue";
import HorizontalBarChart from "./HorizontalBarChart.vue";

export default {
  props: ["program", "finishedCourses", "selectedCourses"],
  components: { VueCal, Conflicts, HorizontalBarChart },
  data: () => ({
    days: [
      { name: "Monday", ab: "Mo." },
      { name: "Tuesday", ab: "Di." },
      { name: "Wednesday", ab: "Mi." },
      { name: "Thurdsay", ab: "Do." },
      { name: "Friday", ab: "Fr." }
    ],
    events: [],
    barOptions: {
      responsive: true,
      maintainAspectRatio: false,
      scales: {
        yAxes: [{ stacked: true }],
        xAxes: [{ stacked: true }]
      }
    },
    barChartData: null,
    bar2Options: {
      responsive: true,
      maintainAspectRatio: false,
      scales: {
        yAxes: [
          {
            ticks: {
              beginAtZero: true
            }
          }
        ],
        xAxes: [
          {
            ticks: {
              beginAtZero: true
            }
          }
        ]
      }
    },
    bar2ChartData: null,
    coursesWithoutTime: []
  }),
  mounted: function() {
    let events = [];
    let coursesWithoutTime = [];

    const dayToDate = {
      "Mo.": "2018-11-19",
      "Di.": "2018-11-20",
      "Mi.": "2018-11-21",
      "Do.": "2018-11-22",
      "Fr.": "2018-11-23"
    };

    for (let i in this.selectedCourses) {
      const course = this.selectedCourses[i];

      const re = /^(\d\d):(\d\d)\sbis\s(\d\d):(\d\d)$/;
      const res = re.exec(course.Time);
      if (!res) {
        coursesWithoutTime.push(course);
        continue;
      }
      const date = dayToDate[course.Day];
      const start = `${date} ${res[1]}:${res[2]}`;
      const end = `${date} ${res[3]}:${res[4]}`;
      events.push({
        start,
        end,
        title: course.Courses,
        class: `color-${i % 10}`
      });
    }

    this.events = events;
    this.coursesWithoutTime = coursesWithoutTime;

    var creditsDone = 0;
    for (let courseName of this.finishedCourses) {
      let course = CourseData.find(
        c => c.Courses === courseName && c.StudyProgram === this.program
      );
      if (course) creditsDone += parseInt(course.Credits);
    }

    const creditsSelected = this.selectedCourses.reduce(
      (c, a) => c + parseInt(a.Credits),
      0
    );

    const totalCredits = this.program.trim().startsWith("B.Sc.") ? 180 : 120;
    const creditsRemaining = totalCredits - (creditsDone + creditsSelected);

    this.barChartData = {
      labels: ["Credits"],
      datasets: [
        {
          label: "Done",
          backgroundColor: "#70ad47",
          data: [creditsDone]
        },
        {
          label: "Selected",
          backgroundColor: "#5d9ad6",
          data: [creditsSelected]
        },
        {
          label: "Remaining",
          backgroundColor: "#ffbf00",
          data: [creditsRemaining]
        }
      ]
    };

    let barDatasets = [];
    const colors = [
      "#e59c2d",
      "#41B883",
      "#E46651",
      "#00D8FF",
      "#ea54e8",
      "#546dea",
      "#29bc9a",
      "#262626",
      "#d1e53b",
      "#d6d8d6"
    ];

    for (let i in this.selectedCourses) {
      let course = this.selectedCourses[i];

      barDatasets.push({
        label: course.Courses,
        backgroundColor: colors[i % colors.length],
        data: [
          course["Study outside course"] === "-"
            ? 0
            : course["Study outside course"],
          course["Realistic expectation"] === "-"
            ? 0
            : course["Realistic expectation"],
          course["Scripts"] === "-" ? 0 : course["Scripts"],
          course["Pace"] === "-" ? 0 : course["Pace"]
        ]
      });
    }

    this.bar2ChartData = {
      labels: [
        "Study outside course",
        "Realistic expectation",
        "Scripts",
        "Pace"
      ],
      datasets: barDatasets
    };
  }
};
</script>

<style>
.vuecal__flex.weekday-label span:last-child {
  display: none;
}
.vuecal__event-time {
  display: none;
}
.vuecal__no-event {
  display: none;
}
.vuecal__event {
  display: flex;
  align-items: center;
  justify-content: center;
}
.vuecal__cell--selected {
  background-color: transparent;
}
.vuecal__event.color-0 {
  background-color: #e59c2d;
  color: #fff;
}
.vuecal__event.color-1 {
  background-color: #41b883;
  color: #fff;
}
.vuecal__event.color-2 {
  background-color: #e46651;
  color: #fff;
}
.vuecal__event.color-3 {
  background-color: #00d8ff;
  color: #fff;
}
.vuecal__event.color-4 {
  background-color: #ea54e8;
  color: #fff;
}
.vuecal__event.color-5 {
  background-color: #546dea;
  color: #fff;
}
.vuecal__event.color-6 {
  background-color: #29bc9a;
  color: #fff;
}
.vuecal__event.color-7 {
  background-color: #262626;
  color: #fff;
}
.vuecal__event.color-8 {
  background-color: #d1e53b;
  color: #fff;
}
.vuecal__event.color-9 {
  background-color: #d6d8d6;
  color: #fff;
}
</style>
