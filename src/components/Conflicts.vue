<template>
  <div>
    <p style="color: red" v-for="(conflict, i) in conflicts" :key="i">
      Warning! {{ conflict[0] }} and {{ conflict[1] }} are in the same time
      slot!
    </p>
  </div>
</template>

<script>
export default {
  props: ["selectedCourses"],
  data: () => ({
    conflicts: []
  }),
  watch: {
    selectedCourses: function(newSelectedCourses) {
      this.recomputeConflicts(newSelectedCourses);
    }
  },
  mounted() {
    this.recomputeConflicts(this.selectedCourses);
  },
  methods: {
    recomputeConflicts(selectedCourses) {
      let days = {};
      for (let course of selectedCourses) {
        if (!days[course.Day]) days[course.Day] = [];
        let x = { course };
        const re = /^(\d\d):(\d\d)\sbis\s(\d\d):(\d\d)$/;
        const res = re.exec(course.Time);
        if (!res) continue;
        x.start = parseInt(res[1]) * 60 + parseInt(res[2]);
        x.end = parseInt(res[3]) * 60 + parseInt(res[4]);
        days[course.Day].push(x);
      }

      let conflicts = [];
      for (let day in days) {
        days[day].sort((a, b) => a.start > b.start);

        for (let i in days[day]) {
          if (i == 0) continue;
          if (days[day][i].start < days[day][i - 1].end) {
            conflicts.push([
              days[day][i - 1].course.Courses,
              days[day][i].course.Courses
            ]);
          }
        }
      }
      this.conflicts = conflicts;
    }
  }
};
</script>
