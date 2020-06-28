<template>
  <div id="app">
    <div class="navbar">
      <a href="#" @click="page = 0">Home</a>
      <a href="#home">About</a>
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
    <HomePage v-if="page === 0" @next="toAddCourse" />
    <AddCourse v-if="page === 1" :program="program" :semester="semester" />
  </div>
</template>

<script>
import HomePage from "./components/HomePage.vue";
import AddCourse from "./components/AddCourse.vue";

export default {
  name: "App",
  components: {
    HomePage,
    AddCourse
  },
  data: () => ({
    page: 0,
    program: "",
    semester: 0
  }),
  methods: {
    toAddCourse({ program, semester }) {
      this.program = program;
      this.semester = semester;
      this.page = 1;
    }
  }
};
</script>

<style>
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
</style>
