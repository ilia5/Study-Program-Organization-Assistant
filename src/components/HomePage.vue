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
          <select name="search_categories" id="season" v-model="selectedSeason">
            <option v-for="season in seasons" :key="season" :value="season">{{
              season
            }}</option>
          </select>
        </div>
      </div>
      <br />
      <input type="submit" value="Submit" @click="nextStep" />
    </div>
  </div>
</template>

<script>
import CourseData from "../AllData.json";

export default {
  data: () => ({
    programs: Array.from(
      new Set(CourseData.map(course => course.StudyProgram))
    ),
    selectedProgram: 0,
    selectedSeason: "WS",
    seasons: ["WS", "SS"]
  }),
  methods: {
    nextStep() {
      this.$emit("next", {
        program: this.programs[this.selectedProgram],
        season: this.selectedSeason
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

h1 {
  color: #2b72af;
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
