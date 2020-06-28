<template>
  <div class="fullheight">
    <h1>Select your courses</h1>
    <p>Select courses that you have completed in previous semesters</p>
    <div class="columns">
      <div class="left">
        <h2>To do</h2>
        <ul
          style="background-color: #f9f9f9; border-radius: 5px; border: solid 1px #aaa; padding: 1rem; list-style: none"
        >
          <li
            v-for="todo in todos"
            :key="todo"
            @click="select(todo)"
            :style="
              `cursor: pointer; ${
                selectedTodo === todo ? 'background-color: #999' : ''
              }`
            "
          >
            {{ todo }}
          </li>
        </ul>
      </div>
      <div class="middle">
        <button @click="add">&gt;</button>
        <button @click="remove">&lt;</button>
        <button @click="removeAll">&lt;&lt;</button>
      </div>
      <div class="right">
        <h2>Completed</h2>
        <ul
          style="background-color: #f9f9f9; border-radius: 5px; border: solid 1px #aaa; padding: 1rem; list-style: none"
        >
          <li
            v-for="todo in finishedCourses"
            :key="todo"
            @click="select(todo)"
            :style="
              `cursor: pointer; ${
                selectedTodo === todo ? 'background-color: #999' : ''
              }`
            "
          >
            {{ todo }}
          </li>
        </ul>
      </div>
    </div>
    <br />
    <input
      type="submit"
      value="Submit"
      style="position: absolute; bottom: 10px; right: 10px"
    />
  </div>
</template>

<script>
import CourseData from "../CourseData.json";

export default {
  props: ["program", "semester"],
  data: function() {
    return {
      todos: CourseData.filter(
        course => course.StudyProgram === this.program
      ).map(course => course.Courses),
      selectedTodo: null,
      finishedCourses: []
    };
  },
  methods: {
    select(todo) {
      if (this.selectedTodo == todo) {
        if (this.finishedCourses.indexOf(todo) >= 0) {
          this.remove();
        } else {
          this.add();
        }
      } else {
        this.selectedTodo = todo;
      }
    },
    add() {
      if (!this.selectedTodo || this.todos.indexOf(this.selectedTodo) < 0)
        return;
      this.todos = this.todos.filter(course => course != this.selectedTodo);
      this.finishedCourses.push(this.selectedTodo);
      this.selectedTodo = null;
    },
    remove() {
      if (
        !this.selectedTodo ||
        this.finishedCourses.indexOf(this.selectedTodo) < 0
      )
        return;
      this.finishedCourses = this.finishedCourses.filter(
        course => course != this.selectedTodo
      );
      this.todos.push(this.selectedTodo);
      this.selectedTodo = null;
    },
    removeAll() {
      this.selectedTodo = null;
      this.todos = this.todos.concat(this.finishedCourses);
      this.finishedCourses = [];
    }
  }
};
</script>

<style>
.columns {
  display: grid;
  grid-template-columns: 2fr 1fr 2fr;
  user-select: none;
}
.middle {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 2rem;
  margin-top: 4rem;
}
.fullheight {
  min-height: calc(100vh - 110px);
  position: relative;
}
</style>
