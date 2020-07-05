<template>
  <div>
    <div style="display: flex; grid-gap: 2rem;">
      <div style="flex: 2;">
        <div>
          <h2>Courses</h2>
          <table>
            <thead>
              <tr>
                <th>Course name</th>
                <th>Lecture</th>
                <th>Exercise</th>
                <th>Practicum</th>
                <th>Seminar</th>
                <th>Time</th>
                <th>Credits</th>
                <th></th>
              </tr>
            </thead>
            <tbody>
              <tr
                v-for="(course, i) in availableCourses"
                :key="i"
                @click="highlightCourse(course)"
                :class="highlightedCourse === course ? 'highlight' : ''"
              >
                <td>{{ course.Courses }}</td>
                <td>{{ course.Lecture }}</td>
                <td>{{ course.Exercise }}</td>
                <td>{{ course.Practicum }}</td>
                <td>{{ course.Seminar }}</td>
                <td>{{ course.Day }} {{ course.Time }}</td>
                <td>{{ course.Credits }}</td>
                <td>
                  <button
                    class="action-button small"
                    @click.stop="addCourse(course)"
                  >
                    Add
                  </button>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
        <p style="font-weight: bold">
          Click on a course to show additional information.
        </p>
        <div>
          <h2>Selected Courses</h2>
          <table>
            <thead>
              <tr>
                <th>Course name</th>
                <th>Lecture</th>
                <th>Exercise</th>
                <th>Practicum</th>
                <th>Seminar</th>
                <th>Time</th>
                <th>Credits</th>
                <th></th>
              </tr>
            </thead>
            <tbody>
              <tr
                v-for="(course, i) in selectedCourses"
                :key="i"
                @click="highlightCourse(course)"
                :class="highlightedCourse === course ? 'highlight' : ''"
              >
                <td>{{ course.Courses }}</td>
                <td>{{ course.Lecture }}</td>
                <td>{{ course.Exercise }}</td>
                <td>{{ course.Practicum }}</td>
                <td>{{ course.Seminar }}</td>
                <td>{{ course.Day }} {{ course.Time }}</td>
                <td>{{ course.Credits }}</td>
                <td>
                  <button
                    class="action-button small"
                    @click.stop="removeCourse(course)"
                  >
                    Remove
                  </button>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
      <div style="flex: 1; margin-top: 4rem">
        <label>Select semester: </label>
        <select v-model="selectedSemester" class="action-button small">
          <option
            v-for="semester in semesters"
            :key="semester"
            :value="semester"
            >{{ semester }}</option
          >
        </select>
        <div v-if="highlightedCourse" style="margin-top: 1rem">
          <strong>{{ highlightedCourse.Courses }}</strong
          ><br />
          <strong>Professor: </strong>{{ highlightedCourse.Professor }}<br />
          <strong>Difficulty: </strong>{{ highlightedCourse.Difficulty }}<br />
          <strong>Usefulness for work: </strong
          >{{ highlightedCourse["Usefulness for work"] }}<br />
          <strong>Room: </strong>{{ highlightedCourse.Room }}<br />
          <a
            :href="highlightedCourse.Link"
            target="_blank"
            style="display: block; margin-top: 0.7rem"
            >Course description</a
          >
        </div>
      </div>
    </div>
    <conflicts :selected-courses="selectedCourses" />
    <div style="display: flex; margin-top: 2rem">
      <div
        style="flex: 1; display: flex; flex-direction: column; align-items: center"
      >
        <pie-chart :chartdata="pieChartdata" :options="pieOptions" />
        <h2 style="">Total Hours: {{ totalHours }}</h2>
      </div>
      <div style="flex: 1">
        <stacked-bar-chart :chartdata="barChartData" :options="barOptions" />
      </div>
    </div>
    <input type="submit" value="Submit" @click="nextStep" />
  </div>
</template>

<script>
import CourseData from "../AllData.json";
import PieChart from "./PieChart.vue";
import StackedBarChart from "./StackedBarChart.vue";
import Conflicts from "./Conflicts.vue";

export default {
  props: ["program", "season", "finishedCourses"],
  components: { PieChart, StackedBarChart, Conflicts },
  data: function() {
    const semesters = Array.from(
      new Set(
        CourseData.filter(course => course.StudyProgram === this.program).map(
          course => course.Semester
        )
      )
    );

    return {
      courseData: CourseData,
      semesters,
      selectedSemester: semesters[0],
      selectedCourses: [],
      highlightedCourse: null,
      pieChartdata: null,
      barChartData: null,
      pieOptions: {
        responsive: true,
        maintainAspectRatio: false
      },
      barOptions: {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
          yAxes: [{ stacked: true }],
          xAxes: [{ stacked: true }]
        }
      },
      totalHours: 0
    };
  },
  computed: {
    availableCourses() {
      return this.courseData.filter(
        course =>
          course.StudyProgram === this.program &&
          course.Semester === this.selectedSemester &&
          course.Season == this.season &&
          !this.finishedCourses.includes(course.Courses) &&
          !this.selectedCourses.includes(course)
      );
    }
  },
  watch: {
    selectedSemester() {
      this.highlightCourse(null);
    }
  },
  methods: {
    addCourse(course) {
      this.selectedCourses = [...this.selectedCourses, course];
      this.dataChanged();
      this.highlightCourse(null);
    },
    removeCourse(course) {
      this.selectedCourses = this.selectedCourses.filter(
        element => element != course
      );
      this.dataChanged();
      this.highlightCourse(null);
    },
    highlightCourse(course) {
      this.highlightedCourse = course;
    },
    dataChanged() {
      let pieDataset = [0, 0, 0, 0];

      for (let course of this.selectedCourses) {
        if (course.Lecture !== "-") pieDataset[0] += course.Lecture;
        if (course.Exercise !== "-") pieDataset[1] += course.Exercise;
        if (course.Practicum !== "-") pieDataset[2] += course.Practicum;
        if (course.Seminar !== "-") pieDataset[3] += course.Seminar;
      }
      this.totalHours = pieDataset.reduce((a, b) => a + b, 0);

      this.pieChartdata = {
        labels: ["Lectures", "Exercise", "Practicum", "Seminar"],
        datasets: [
          {
            label: "Total Hours",
            backgroundColor: ["#e59c2d", "#41B883", "#E46651", "#00D8FF"],
            data: pieDataset
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
            course.Lecture === "-" ? 0 : course.Lecture,
            course.Exercise === "-" ? 0 : course.Exercise,
            course.Practicum === "-" ? 0 : course.Practicum,
            course.Seminar === "-" ? 0 : course.Seminar
          ]
        });
      }

      this.barChartData = {
        labels: ["Lectures", "Exercise", "Practicum", "Seminar"],
        datasets: barDatasets
      };
    },
    nextStep() {
      this.$emit("next", {
        selectedCourses: this.selectedCourses
      });
    }
  }
};
</script>

<style>
.highlight {
  background-color: #f2d79d !important;
}
table {
  border: solid 1px #bdbdbd;
  margin: 1rem 0;
}
table thead tr {
  background-color: #ddd;
  text-align: left;
}
table tbody tr:nth-child(2n) {
  background-color: #eee;
}
td,
th {
  padding: 3px 6px;
}
</style>
