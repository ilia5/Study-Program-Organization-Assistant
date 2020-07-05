<template>
  <div id="app">
    <div class="navbar">
      <a href="#" @click="page = 0">Home</a>
      <a href="#" @click="page = 100">About</a>
      <div class="dropdown">
        <button class="dropbtn">
          Main Sources
          <i class="fa fa-caret-down"></i>
        </button>
        <div class="dropdown-content">
          <a href="https://moodle.uni-due.de/course/view.php?id=2032"
            >Source 1</a
          >
          <a href="https://www.uni-due.de/vdb/studiengang/liste">Source 2</a>
          <a href="https://campus.uni-due.de/lsf/rds?state=user&type=0"
            >Source 3</a
          >
        </div>
      </div>
    </div>
    <div style="padding: 0 4rem;">
      <HomePage v-if="page === 0" @next="toAddCourse" />
      <AddCourse
        v-if="page === 1"
        :program="program"
        :season="season"
        @next="toSemesterCourses"
      />
      <SemesterCourses
        v-if="page === 2"
        :program="program"
        :season="season"
        :finishedCourses="finishedCourses"
        @next="toTimeTable"
      />
      <TimeTable
        v-if="page === 3"
        :program="program"
        :finishedCourses="finishedCourses"
        :selectedCourses="selectedCourses"
        @next="toTimeTable"
      />
      <About v-if="page === 100" />
    </div>
  </div>
</template>

<script>
import HomePage from "./components/HomePage.vue";
import AddCourse from "./components/AddCourse.vue";
import SemesterCourses from "./components/SemesterCourses.vue";
import TimeTable from "./components/TimeTable.vue";
import About from "./components/About.vue";

export default {
  name: "App",
  components: {
    HomePage,
    AddCourse,
    SemesterCourses,
    TimeTable,
    About
  },
  data: () => ({
    page: 0,
    program: "",
    season: 0,
    finishedCourses: [],
    selectedCourses: []
  }),
  methods: {
    toAddCourse({ program, season }) {
      this.program = program;
      this.season = season;
      this.page = 1;
    },
    toSemesterCourses({ finishedCourses }) {
      this.finishedCourses = finishedCourses;
      this.page = 2;
    },
    toTimeTable({ selectedCourses }) {
      this.selectedCourses = selectedCourses;
      this.page = 3;
    }
  }
};
</script>

<style>
body {
  padding: 0;
  margin: 0;
  font-family: "Rockwell", Helvetica, sans-serif;
}

.navbar {
  overflow: hidden;
  background-color: #333;
}

.navbar a {
  float: left;
  font-size: 20px;
  color: white;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
}

/* Header Design */

.dropdown {
  float: left;
  overflow: hidden;
}

.dropdown .dropbtn {
  font-size: 20px;
  border: none;
  outline: none;
  color: white;
  padding: 14px 16px;
  background-color: inherit;
  font-family: inherit;
  margin: 0;
}

.navbar a:hover,
.dropdown:hover .dropbtn {
  background-color: red;
}

.dropdown-content {
  display: none;
  position: absolute;
  background-color: #f9f9f9;
  min-width: 160px;
  box-shadow: 0px 8px 16px 0px rgba(0, 0, 0, 0.2);
  z-index: 1;
}

.dropdown-content a {
  float: none;
  color: black;
  padding: 12px 16px;
  text-decoration: none;
  display: block;
  text-align: left;
}

.dropdown-content a:hover {
  background-color: #ddd;
}

.dropdown:hover .dropdown-content {
  display: block;
}
/*End of Header design  */

table {
  width: 100%;
}

.action-button {
  background-color: #333;
  color: white;
  padding: 1rem 2rem;
  border: solid 1px #666;
  border-radius: 5px;
  cursor: pointer;
}
.action-button.small {
  padding: 3px 6px;
}
.action-button:hover {
  background-color: #444;
}
</style>
