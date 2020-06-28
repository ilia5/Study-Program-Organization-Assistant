<template>
  <div>
    <br /><br /><br />
    <H1>Study Program Organization Assistant</H1>
    <div class="study_program_selection_position">
      <h2>Select Your Study Program:</h2>
      <div class="select_categories">
        <div class="select">
          <select
            name="search_categories"
            id="study_program"
            v-model="selectedProgram"
          >
            <option v-for="(program, i) in programs" :key="i" :value="i">{{
              program
            }}</option>
          </select>
        </div>
      </div>
      <br />
      <h2>Select Your Semester:</h2>
      <div class="select_categories">
        <div class="select">
          <select
            name="search_categories"
            id="semester"
            v-model="selectedSemester"
          >
            <option
              v-for="semester in numberOfSemesters"
              :key="semester"
              :value="semester"
              >{{ semester }}</option
            >
          </select>
        </div>
      </div>
      <br />
      <input type="submit" value="Submit" @click="nextStep" />
    </div>
  </div>
</template>

<script>
import CourseData from "../CourseData.json";

export default {
  data: () => ({
    programs: Array.from(
      new Set(CourseData.map(course => course.StudyProgram))
    ),
    selectedProgram: 0,
    selectedSemester: 1
  }),
  computed: {
    numberOfSemesters() {
      if (this.programs[this.selectedProgram].indexOf("B.Sc") === 0) {
        return 6;
      }
      return 4;
    }
  },
  methods: {
    nextStep() {
      this.$emit("next", {
        program: this.programs[this.selectedProgram],
        semester: this.selectedSemester
      });
    }
  }
};
</script>

<style>
.select_categories {
  font-size: 20px;
  padding: 10px 8px 10px 14px;
  background: #fff;
  border: 1px solid #ccc;
  border-radius: 6px;
  overflow: hidden;
  position: relative;
}

.select_categories .select {
  width: 100%;
  background-position: 100% center;
}

.select_categories .select select {
  background: transparent;
  line-height: 1;
  border: 0;
  padding: 0;
  border-radius: 0;
  width: 100%;
  position: relative;
  z-index: 10;
  font-size: 1em;
}
div.study_program_selection_position {
  position: absolute;
  width: 500px;
  height: 200px;
  z-index: 15;
  top: 50%;
  left: 45%;
  margin: -100px 0 0 -150px;
}
body {
  font-family: "Rockwell", Helvetica, sans-serif;
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

h1 {
  color: red;
  text-shadow: shadow1, shadow2, shadow3;
  text-shadow: 4px 3px 0px #fff, 9px 8px 0px rgba(0, 0, 0, 0.15);
  text-align: center;
  font-size: 55px;
}

input[type="submit"] {
  background-color: #333;
  border: none;
  color: white;
  padding: 20px 32px;
  font-size: 20px;
  text-decoration: none;
  margin: 4px 2px;
  cursor: pointer;
  position: absolute;
  right: 0;
}
</style>
